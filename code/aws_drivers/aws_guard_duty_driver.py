import boto3

from flask import current_app
from api.errors import GuardDutyError
from botocore.exceptions import (
    BotoCoreError,
    ClientError
)


class GuardDutyDriver(object):
    """
    Class for working with AWS GuardDuty resource
    """

    def __init__(self):
        self.region = str(current_app.config['AWS_REGION'])
        self.access_key = str(current_app.config['AWS_ACCESS_KEY_ID'])
        self.secret_key = str(current_app.config['AWS_SECRET_ACCESS_KEY'])
        self.driver = boto3.client(
            'guardduty', self.region,
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key
        )
        self.findings = self.Finding(self)

    class Finding:

        def __init__(self, root):
            self._findings = []
            self.max_results = 50
            self.driver = root.driver
            self.ctr_limit = current_app.config['CTR_ENTITIES_LIMIT']
            self.detector = current_app.config['AWS_GUARD_DUTY_DETECTOR_ID']

        def get(self):
            return self._findings

        def list_by(self, criterion, limit=None, next_token=''):
            try:
                limit = self.ctr_limit if not limit else limit

                response = self.driver.list_findings(
                    DetectorId=self.detector,
                    FindingCriteria=criterion,
                    MaxResults=limit if limit <= self.max_results
                    else self.max_results,
                    NextToken=next_token
                )

                findings = self.driver.get_findings(
                    DetectorId=self.detector,
                    FindingIds=response.get('FindingIds')
                ).get('Findings')

                for finding in findings:
                    if len(self._findings) < self.ctr_limit \
                            and finding not in self._findings:
                        self._findings.append(finding)
            except (BotoCoreError, ValueError, ClientError) as error:
                raise GuardDutyError(error.args[0])

            next_token = response.get('NextToken')
            if next_token and len(self._findings) < self.ctr_limit:
                self.list_by(criterion, limit - self.max_results, next_token)
