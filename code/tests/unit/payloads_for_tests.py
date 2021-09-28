from datetime import datetime

EXPECTED_RESPONSE_OF_JWKS_ENDPOINT = {
    "keys": [
        {
            "kty": "RSA",
            "n": "tSKfSeI0fukRIX38AHlKB1YPpX8PUYN2JdvfM-XjNmLfU1M74N0V"
                 "mdzIX95sneQGO9kC2xMIE-AIlt52Yf_KgBZggAlS9Y0Vx8DsSL2H"
                 "vOjguAdXir3vYLvAyyHin_mUisJOqccFKChHKjnk0uXy_38-1r17"
                 "_cYTp76brKpU1I4kM20M__dbvLBWjfzyw9ehufr74aVwr-0xJfsB"
                 "Vr2oaQFww_XHGz69Q7yHK6DbxYO4w4q2sIfcC4pT8XTPHo4JZ2M7"
                 "33Ea8a7HxtZS563_mhhRZLU5aynQpwaVv2U--CL6EvGt8TlNZOke"
                 "Rv8wz-Rt8B70jzoRpVK36rR-pHKlXhMGT619v82LneTdsqA25Wi2"
                 "Ld_c0niuul24A6-aaj2u9SWbxA9LmVtFntvNbRaHXE1SLpLPoIp8"
                 "uppGF02Nz2v3ld8gCnTTWfq_BQ80Qy8e0coRRABECZrjIMzHEg6M"
                 "loRDy4na0pRQv61VogqRKDU2r3_VezFPQDb3ciYsZjWBr3HpNOkU"
                 "jTrvLmFyOE9Q5R_qQGmc6BYtfk5rn7iIfXlkJAZHXhBy-ElBuiBM"
                 "-YSkFM7dH92sSIoZ05V4MP09Xcppx7kdwsJy72Sust9Hnd9B7V35"
                 "YnVF6W791lVHnenhCJOziRmkH4xLLbPkaST2Ks3IHH7tVltM6NsR"
                 "k3jNdVM",
            "e": "AQAB",
            "alg": "RS256",
            "kid": "02B1174234C29F8EFB69911438F597FF3FFEE6B7",
            "use": "sig"
        }
    ]
}

RESPONSE_OF_JWKS_ENDPOINT_WITH_WRONG_KEY = {
    "keys": [
        {
            "kty": "RSA",
            "n": "pSKfSeI0fukRIX38AHlKB1YPpX8PUYN2JdvfM-XjNmLfU1M74N0V"
                 "mdzIX95sneQGO9kC2xMIE-AIlt52Yf_KgBZggAlS9Y0Vx8DsSL2H"
                 "vOjguAdXir3vYLvAyyHin_mUisJOqccFKChHKjnk0uXy_38-1r17"
                 "_cYTp76brKpU1I4kM20M__dbvLBWjfzyw9ehufr74aVwr-0xJfsB"
                 "Vr2oaQFww_XHGz69Q7yHK6DbxYO4w4q2sIfcC4pT8XTPHo4JZ2M7"
                 "33Ea8a7HxtZS563_mhhRZLU5aynQpwaVv2U--CL6EvGt8TlNZOke"
                 "Rv8wz-Rt8B70jzoRpVK36rR-pHKlXhMGT619v82LneTdsqA25Wi2"
                 "Ld_c0niuul24A6-aaj2u9SWbxA9LmVtFntvNbRaHXE1SLpLPoIp8"
                 "uppGF02Nz2v3ld8gCnTTWfq_BQ80Qy8e0coRRABECZrjIMzHEg6M"
                 "loRDy4na0pRQv61VogqRKDU2r3_VezFPQDb3ciYsZjWBr3HpNOkU"
                 "jTrvLmFyOE9Q5R_qQGmc6BYtfk5rn7iIfXlkJAZHXhBy-ElBuiBM"
                 "-YSkFM7dH92sSIoZ05V4MP09Xcppx7kdwsJy72Sust9Hnd9B7V35"
                 "YnVF6W791lVHnenhCJOziRmkH4xLLbPkaST2Ks3IHH7tVltM6NsR"
                 "k3jNdVM",
            "e": "AQAB",
            "alg": "RS256",
            "kid": "02B1174234C29F8EFB69911438F597FF3FFEE6B7",
            "use": "sig"
        }
    ]
}

PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIJKwIBAAKCAgEAtSKfSeI0fukRIX38AHlKB1YPpX8PUYN2JdvfM+XjNmLfU1M7
4N0VmdzIX95sneQGO9kC2xMIE+AIlt52Yf/KgBZggAlS9Y0Vx8DsSL2HvOjguAdX
ir3vYLvAyyHin/mUisJOqccFKChHKjnk0uXy/38+1r17/cYTp76brKpU1I4kM20M
//dbvLBWjfzyw9ehufr74aVwr+0xJfsBVr2oaQFww/XHGz69Q7yHK6DbxYO4w4q2
sIfcC4pT8XTPHo4JZ2M733Ea8a7HxtZS563/mhhRZLU5aynQpwaVv2U++CL6EvGt
8TlNZOkeRv8wz+Rt8B70jzoRpVK36rR+pHKlXhMGT619v82LneTdsqA25Wi2Ld/c
0niuul24A6+aaj2u9SWbxA9LmVtFntvNbRaHXE1SLpLPoIp8uppGF02Nz2v3ld8g
CnTTWfq/BQ80Qy8e0coRRABECZrjIMzHEg6MloRDy4na0pRQv61VogqRKDU2r3/V
ezFPQDb3ciYsZjWBr3HpNOkUjTrvLmFyOE9Q5R/qQGmc6BYtfk5rn7iIfXlkJAZH
XhBy+ElBuiBM+YSkFM7dH92sSIoZ05V4MP09Xcppx7kdwsJy72Sust9Hnd9B7V35
YnVF6W791lVHnenhCJOziRmkH4xLLbPkaST2Ks3IHH7tVltM6NsRk3jNdVMCAwEA
AQKCAgEArx+0JXigDHtFZr4pYEPjwMgCBJ2dr8+L8PptB/4g+LoK9MKqR7M4aTO+
PoILPXPyWvZq/meeDakyZLrcdc8ad1ArKF7baDBpeGEbkRA9JfV5HjNq/ea4gyvD
MCGou8ZPSQCnkRmr8LFQbJDgnM5Za5AYrwEv2aEh67IrTHq53W83rMioIumCNiG+
7TQ7egEGiYsQ745GLrECLZhKKRTgt/T+k1cSk1LLJawme5XgJUw+3D9GddJEepvY
oL+wZ/gnO2ADyPnPdQ7oc2NPcFMXpmIQf29+/g7FflatfQhkIv+eC6bB51DhdMi1
zyp2hOhzKg6jn74ixVX+Hts2/cMiAPu0NaWmU9n8g7HmXWc4+uSO/fssGjI3DLYK
d5xnhrq4a3ZO5oJLeMO9U71+Ykctg23PTHwNAGrsPYdjGcBnJEdtbXa31agI5PAG
6rgGUY3iSoWqHLgBTxrX04TWVvLQi8wbxh7BEF0yasOeZKxdE2IWYg75zGsjluyH
lOnpRa5lSf6KZ6thh9eczFHYtS4DvYBcZ9hZW/g87ie28SkBFxxl0brYt9uKNYJv
uajVG8kT80AC7Wzg2q7Wmnoww3JNJUbNths5dqKyUSlMFMIB/vOePFHLrA6qDfAn
sQHgUb9WHhUrYsH20XKpqR2OjmWU05bV4pSMW/JwG37o+px1yKECggEBANnwx0d7
ksEMvJjeN5plDy3eMLifBI+6SL/o5TXDoFM6rJxF+0UP70uouYJq2dI+DCSA6c/E
sn7WAOirY177adKcBV8biwAtmKHnFnCs/kwAZq8lMvQPtNPJ/vq2n40kO48h8fxb
eGcmyAqFPZ4YKSxrPA4cdbHIuFSt9WyaUcVFmzdTFHVlRP70EXdmXHt84byWNB4C
Heq8zmrNxPNAi65nEkUks7iBQMtuvyV2+aXjDOTBMCd66IhIh2iZq1O7kXUwgh1O
H9hCa7oriHyAdgkKdKCWocmbPPENOETgjraA9wRIXwOYTDb1X5hMvi1mCHo8xjMj
u4szD03xJVi7WrsCggEBANTEblCkxEyhJqaMZF3U3df2Yr/ZtHqsrTr4lwB/MOKk
zmuSrROxheEkKIsxbiV+AxTvtPR1FQrlqbhTJRwy+pw4KPJ7P4fq2R/YBqvXSNBC
amTt6l2XdXqnAk3A++cOEZ2lU9ubfgdeN2Ih8rgdn1LWeOSjCWfExmkoU61/Xe6x
AMeXKQSlHKSnX9voxuE2xINHeU6ZAKy1kGmrJtEiWnI8b8C4s8fTyDtXJ1Lasys0
iHO2Tz2jUhf4IJwb87Lk7Ize2MrI+oPzVDXlmkbjkB4tYyoiRTj8rk8pwBW/HVv0
02pjOLTa4kz1kQ3lsZ/3As4zfNi7mWEhadmEsAIfYkkCggEBANO39r/Yqj5kUyrm
ZXnVxyM2AHq58EJ4I4hbhZ/vRWbVTy4ZRfpXeo4zgNPTXXvCzyT/HyS53vUcjJF7
PfPdpXX2H7m/Fg+8O9S8m64mQHwwv5BSQOecAnzkdJG2q9T/Z+Sqg1w2uAbtQ9QE
kFFvA0ClhBfpSeTGK1wICq3QVLOh5SGf0fYhxR8wl284v4svTFRaTpMAV3Pcq2JS
N4xgHdH1S2hkOTt6RSnbklGg/PFMWxA3JMKVwiPy4aiZ8DhNtQb1ctFpPcJm9CRN
ejAI06IAyD/hVZZ2+oLp5snypHFjY5SDgdoKL7AMOyvHEdEkmAO32ot/oQefOLTt
GOzURVUCggEBALSx5iYi6HtT2SlUzeBKaeWBYDgiwf31LGGKwWMwoem5oX0GYmr5
NwQP20brQeohbKiZMwrxbF+G0G60Xi3mtaN6pnvYZAogTymWI4RJH5OO9CCnVYUK
nkD+GRzDqqt97UP/Joq5MX08bLiwsBvhPG/zqVQzikdQfFjOYNJV+wY92LWpELLb
Lso/Q0/WDyExjA8Z4lH36vTCddTn/91Y2Ytu/FGmCzjICaMrzz+0cLlesgvjZsSo
MY4dskQiEQN7G9I/Z8pAiVEKlBf52N4fYUPfs/oShMty/O5KPNG7L0nrUKlnfr9J
rStC2l/9FK8P7pgEbiD6obY11FlhMMF8udECggEBAIKhvOFtipD1jqDOpjOoR9sK
/lRR5bVVWQfamMDN1AwmjJbVHS8hhtYUM/4sh2p12P6RgoO8fODf1vEcWFh3xxNZ
E1pPCPaICD9i5U+NRvPz2vC900HcraLRrUFaRzwhqOOknYJSBrGzW+Cx3YSeaOCg
nKyI8B5gw4C0G0iL1dSsz2bR1O4GNOVfT3R6joZEXATFo/Kc2L0YAvApBNUYvY0k
bjJ/JfTO5060SsWftf4iw3jrhSn9RwTTYdq/kErGFWvDGJn2MiuhMe2onNfVzIGR
mdUxHwi1ulkspAn/fmY7f0hZpskDwcHyZmbKZuk+NU/FJ8IAcmvk9y7m25nSSc8=
-----END RSA PRIVATE KEY-----"""

TILES_RESPONSE = {
    "data": [
        {
            "default_period": "last_7_days",
            "description": ("Affected Instances chart shows what"
                            " types of findings EC2 instances have."),
            "id": "affected_instances",
            "periods": [
                "last_24_hours",
                "last_7_days",
                "last_30_days"
            ],
            "short_description": ("Affected Instances by finding "
                                  "types for given time period."),
            "tags": [
                "affected_instances"
            ],
            "title": "Affected instances",
            "type": "donut_graph"
        }
    ]
}

AFFECTED_INSTANCES_CRITERIA = {
    "Criterion": {
        "resource.resourceType": {
            "Equals": [
                "Instance"
            ]
        },
        "updatedAt": {
            "Gt": 1631653200,
        }
    }
}

OBSERVE_RESPONSE = {
    "data": {
        "indicators": {
            "count": 2,
            "docs": [
                {
                    "confidence": "High",
                    "description": "EC2 instance i-99999999 is "
                                   "querying a domain name of a "
                                   "remote host that is a "
                                   "known source "
                                   "of Drive-By download attacks.",
                    "external_ids": [
                        "aws-guard-duty-indicator-31b81b20c7d6b9d"
                        "add40c06eb8bf1ad079c7e4f96d2be00660f6da9"
                        "b82421335"
                    ],
                    "id": "transient:aws-guard-duty-indicator-"
                          "f001da94620f4d2e8f0fe6d29629e618",
                    "producer": "network.ips",
                    "schema_version": "1.0.17",
                    "severity": "High",
                    "short_description": "EC2 instance i-99999999 "
                                         "is querying a domain "
                                         "name of a remote host that "
                                         "is a known "
                                         "source of Drive-By "
                                         "download attacks.",
                    "source": "Amazon GuardDuty findings",
                    "source_uri": "https://console.aws.amazon.com"
                                  "/guardduty/home?region/"
                                  "findings&region=region"
                                  "#/findings?macros"
                                  "=all&fId=0ebd952561ab2299"
                                  "30385cfe43860cbf&search=id"
                                  "%3D0ebd952561ab229930385c"
                                  "fe43860cbf",
                    "timestamp": "2021-08-09T09:42:27.000Z",
                    "type": "indicator",
                    "valid_time": {
                        "end_time": "2525-01-01T00:00:00.000Z",
                        "start_time": "2021-08-09T09:42:27.000Z"
                    }
                },
                {
                    "confidence": "High",
                    "description": "EC2 instance i-99999999 is "
                                   "querying a domain name "
                                   "associated with a known "
                                   "Command & Control "
                                   "server.",
                    "external_ids": [
                        "aws-guard-duty-indicator-"
                        "31b81b20c7d6b9dadd40c06eb8bf1ad079c7"
                        "e4f96d2be00660f6da9b82421335"
                    ],
                    "id": "transient:aws-guard-duty-"
                          "indicator-88c24095ae564d57"
                          "95cc3f08992e5898",
                    "producer": "network.ips",
                    "schema_version": "1.0.17",
                    "severity": "High",
                    "short_description": "EC2 instance i-99999999 "
                                         "is querying a domain "
                                         "name associated with a "
                                         "known Command & "
                                         "Control server.",
                    "source": "Amazon GuardDuty findings",
                    "source_uri": "https://console.aws.amazon.com/"
                                  "guardduty/home?region/findings&"
                                  "region=region"
                                  "#/findings?macros"
                                  "=all&fId=14bd952561ab40e0b927"
                                  "5f648fcca0f2&search=id"
                                  "%3D14bd952561ab40e0b9275f648fcca0f2",
                    "timestamp": "2021-08-09T09:42:27.000Z",
                    "type": "indicator",
                    "valid_time": {
                        "end_time": "2525-01-01T00:00:00.000Z",
                        "start_time": "2021-08-09T09:42:27.000Z"
                    }
                }
            ]
        },
        "relationships": {
            "count": 2,
            "docs": [
                {
                    "external_ids": [
                        "aws-guard-duty-relationship-"
                        "198e4e9957b34070f57e69942dd2"
                        "c751c72e5dfd41e7ab2ac47f4b26766d7a69"
                    ],
                    "id": "transient:aws-guard-duty-relationship"
                          "-08c0d67d19e5483998953246c094fe0d",
                    "relationship_type": "sighting-of",
                    "schema_version": "1.0.17",
                    "source": "Amazon GuardDuty findings",
                    "source_ref": "transient:aws-guard-duty-"
                                  "sighting-099065c8932f41e2908"
                                  "3ed7a742cb644",
                    "source_uri": "https://console.aws.amazon.com/"
                                  "guardduty/home?region/"
                                  "findings&region=region"
                                  "#/findings?macros"
                                  "=all&fId=0ebd952561ab22993038"
                                  "5cfe43860cbf&search=id"
                                  "%3D0ebd952561ab229930385cfe"
                                  "43860cbf",
                    "target_ref": "transient:aws-guard-duty-"
                                  "indicator-f001da94620f4d2e8f0"
                                  "fe6d29629e618",
                    "type": "relationship"
                },
                {
                    "external_ids": [
                        "aws-guard-duty-relationship-"
                        "198e4e9957b34070f57e69942dd2"
                        "c751c72e5dfd41e7ab2ac47f4b26766d7a69"
                    ],
                    "id": "transient:aws-guard-duty-relationship"
                          "-10774be950d74376bc1bd90a98e89d21",
                    "relationship_type": "sighting-of",
                    "schema_version": "1.0.17",
                    "source": "Amazon GuardDuty findings",
                    "source_ref": "transient:aws-guard-duty-"
                                  "sighting-bc0af638cea2466cb"
                                  "74e34d4dcd3fc4b",
                    "source_uri": "https://console.aws.amazon.com/"
                                  "guardduty/home?region/findings"
                                  "&region=region"
                                  "#/findings?macros"
                                  "=all&fId=14bd952561ab40e0b92"
                                  "75f648fcca0f2&search=id"
                                  "%3D14bd952561ab40e0b9275f648f"
                                  "cca0f2",
                    "target_ref": "transient:aws-guard-duty-"
                                  "indicator-88c24095ae564d5795"
                                  "cc3f08992e5898",
                    "type": "relationship"
                }
            ]
        },
        "sightings": {
            "count": 2,
            "docs": [
                {
                    "confidence": "High",
                    "count": 3,
                    "description": "EC2 instance i-99999999 is "
                                   "querying a domain name of "
                                   "a remote host that is a "
                                   "known source "
                                   "of Drive-By download attacks.",
                    "external_ids": [
                        "aws-guard-duty-sighting-7a830ab68800aff"
                        "6a15e61294b41a4e07d177c495f49ee808d232"
                        "e719e5a34bd"
                    ],
                    "id": "transient:aws-guard-duty-sighting-"
                          "099065c8932f41e29083ed7a742cb644",
                    "internal": True,
                    "observables": [
                        {
                            "type": "ip",
                            "value": "10.0.0.1"
                        }
                    ],
                    "observed_time": {
                        "end_time": "2021-09-20T14:24:35.000Z",
                        "start_time": "2021-08-09T09:42:27.000Z"
                    },
                    "relations": [],
                    "schema_version": "1.0.17",
                    "sensor": "network.ips",
                    "severity": "High",
                    "source": "Amazon GuardDuty findings",
                    "source_uri": "https://console.aws.amazon.com/"
                                  "guardduty/home?region/findings"
                                  "&region=region"
                                  "#/findings?macros=all&fId="
                                  "0ebd952561ab229930385cfe43860cb"
                                  "f&search=id"
                                  "%3D0ebd952561ab229930385cfe43"
                                  "860cbf",
                    "targets": [
                        {
                            "observables": [
                                {
                                    "type": "ip",
                                    "value": "198.51.100.0"
                                },
                                {
                                    "type": "ip",
                                    "value": "10.0.0.1"
                                },
                                {
                                    "type": "domain",
                                    "value": "GeneratedFindingPu"
                                             "blicDNSName"
                                }
                            ],
                            "observed_time": {
                                "end_time": "2021-09-20T14:24:35.000Z",
                                "start_time": "2021-08-09T09:42:27.000Z"
                            },
                            "type": "network.ips"
                        }
                    ],
                    "timestamp": "2021-09-20T14:24:35.000Z",
                    "title": "Drive-by source domain name queried "
                             "by EC2 instance i-99999999.",
                    "type": "sighting"
                },
                {
                    "confidence": "High",
                    "count": 3,
                    "description": "EC2 instance i-99999999 is "
                                   "querying a domain name "
                                   "associated with a known "
                                   "Command & Control "
                                   "server.",
                    "external_ids": [
                        "aws-guard-duty-sighting-0732a5b0377c7e"
                        "48d57e23f71c193220902192eb21c7d52159"
                        "fd819c9c4dc228"
                    ],
                    "id": "transient:aws-guard-duty-sighting-"
                          "bc0af638cea2466cb74e34d4dcd3fc4b",
                    "internal": True,
                    "observables": [
                        {
                            "type": "ip",
                            "value": "10.0.0.1"
                        }
                    ],
                    "observed_time": {
                        "end_time": "2021-09-20T14:24:35.000Z",
                        "start_time": "2021-08-09T09:42:27.000Z"
                    },
                    "relations": [],
                    "schema_version": "1.0.17",
                    "sensor": "network.ips",
                    "severity": "High",
                    "source": "Amazon GuardDuty findings",
                    "source_uri": "https://console.aws.amazon.com/"
                                  "guardduty/home?region/findings"
                                  "&region=region"
                                  "#/findings?macros=all&fId="
                                  "14bd952561ab40e0b9275f648"
                                  "fcca0f2&search=id"
                                  "%3D14bd952561ab40e0b9275f"
                                  "648fcca0f2",
                    "targets": [
                        {
                            "observables": [
                                {
                                    "type": "ip",
                                    "value": "198.51.100.0"
                                },
                                {
                                    "type": "ip",
                                    "value": "10.0.0.1"
                                },
                                {
                                    "type": "domain",
                                    "value": "GeneratedFind"
                                             "ingPublicDNSName"
                                }
                            ],
                            "observed_time": {
                                "end_time": "2021-09-20T14:24:35.000Z",
                                "start_time": "2021-08-09T09:42:27.000Z"
                            },
                            "type": "network.ips"
                        }
                    ],
                    "timestamp": "2021-09-20T14:24:35.000Z",
                    "title": "Command and Control server domain "
                             "name queried by EC2 instance i-99999999.",
                    "type": "sighting"
                }
            ]
        }
    }
}

REFER_RESPONSE = {
    "data": [
        {
            "categories": [
                "Search",
                "Amazon Detective"
            ],
            "description": "Check this IP with Amazon Detective",
            "id": "ref-aws-detective-search-ip-10.0.0.1",
            "title": "Search for this IP",
            "url": "https://region.console.aws.amazon.com/"
                   "detective/home?region=region#entities/IpAddress/10.0.0.1"
        }
    ]
}


def guard_duty_response():
    return [
        {
            "AccountId": "id",
            "Arn": "arn:aws:guardduty:us-east-2:id:detector/"
                   "detector_id/finding/"
                   "0ebd952561ab229930385cfe43860cbf",
            "CreatedAt": "2021-08-09T09:42:27.926Z",
            "Description": "EC2 instance i-99999999 is querying "
                           "a domain name of a "
                           "remote host that is a known source "
                           "of Drive-By download attacks.",
            "Id": "0ebd952561ab229930385cfe43860cbf",
            "Partition": "aws",
            "Region": "us-east-2",
            "Resource": {
                "InstanceDetails": {
                    "AvailabilityZone": "GeneratedFinding"
                                        "InstaceAvailabilityZone",
                    "IamInstanceProfile": {
                        "Arn": "arn:aws:iam::id:example/instance/profile",
                        "Id": "GeneratedFindingInstanceProfileId"
                    },
                    "ImageDescription": "GeneratedFinding"
                                        "InstaceImageDescription",
                    "ImageId": "ami-99999999",
                    "InstanceId": "i-99999999",
                    "InstanceState": "running",
                    "InstanceType": "m3.xlarge",
                    "OutpostArn": "arn:aws:outposts:us-west-2:id:"
                                  "outpost/op-0fbc006e9abbc73c3",
                    "LaunchTime": "2016-07-16T15:55:03.000Z",
                    "NetworkInterfaces": [
                        {
                            "Ipv6Addresses": [],
                            "NetworkInterfaceId": "eni-bfcffe88",
                            "PrivateDnsName": "GeneratedFindingPrivateDnsName",
                            "PrivateIpAddress": "10.0.0.1",
                            "PrivateIpAddresses": [
                                {
                                    "PrivateDnsName": "Generated"
                                                      "FindingPrivateName",
                                    "PrivateIpAddress": "10.0.0.1"
                                }
                            ],
                            "PublicDnsName": "GeneratedFindingPublicDNSName",
                            "PublicIp": "198.51.100.0",
                            "SecurityGroups": [
                                {
                                    "GroupId": "GeneratedFindingSecurityId",
                                    "GroupName": "GeneratedFinding"
                                                 "SecurityGroupName"
                                }
                            ],
                            "SubnetId": "GeneratedFindingSubnetId",
                            "VpcId": "GeneratedFindingVPCId"
                        }
                    ],
                    "ProductCodes": [
                        {}
                    ],
                    "Tags": [
                        {
                            "Key": "GeneratedFindingInstaceTag1",
                            "Value": "GeneratedFindingInstaceValue1"
                        },
                        {
                            "Key": "GeneratedFindingInstaceTag2",
                            "Value": "GeneratedFindingInstaceTagValue2"
                        },
                        {
                            "Key": "GeneratedFindingInstaceTag3",
                            "Value": "GeneratedFindingInstaceTagValue3"
                        },
                        {
                            "Key": "GeneratedFindingInstaceTag4",
                            "Value": "GeneratedFindingInstaceTagValue4"
                        },
                        {
                            "Key": "GeneratedFindingInstaceTag5",
                            "Value": "GeneratedFindingInstaceTagValue5"
                        },
                        {
                            "Key": "GeneratedFindingInstaceTag6",
                            "Value": "GeneratedFindingInstaceTagValue6"
                        },
                        {
                            "Key": "GeneratedFindingInstaceTag7",
                            "Value": "GeneratedFindingInstaceTagValue7"
                        },
                        {
                            "Key": "GeneratedFindingInstaceTag8",
                            "Value": "GeneratedFindingInstaceTagValue8"
                        },
                        {
                            "Key": "GeneratedFindingInstaceTag9",
                            "Value": "GeneratedFindingInstaceTagValue9"
                        }
                    ]
                },
                "ResourceType": "Instance"
            },
            "SchemaVersion": "2.0",
            "Service": {
                "Action": {
                    "ActionType": "DNS_REQUEST",
                    "DnsRequestAction": {
                        "Domain": "GeneratedFindingDomainName"
                    }
                },
                "Evidence": {
                    "ThreatIntelligenceDetails": [
                        {
                            "ThreatListName": "GeneratedFindingThreatListName",
                            "ThreatNames": [
                                "GeneratedFindingThreatName"
                            ]
                        }
                    ]
                },
                "Archived": False,
                "Count": 3,
                "DetectorId": "detector_id",
                "EventFirstSeen": "2021-08-09T09:42:27.000Z",
                "EventLastSeen": "2021-09-20T14:24:35.000Z",
                "ResourceRole": "TARGET",
                "ServiceName": "guardduty"
            },
            "Severity": 8,
            "Title": "Drive-by source domain "
                     "name queried by EC2 instance i-99999999.",
            "Type": "Trojan:EC2/DriveBySourceTraffic!DNS",
            "UpdatedAt": "2021-09-20T14:24:35.130Z"
        },
        {
            "AccountId": "id",
            "Arn": "arn:aws:guardduty:us-east-2:id:detector/"
                   "detector_id/finding/14bd952561ab40e0b9275f648fcca0f2",
            "CreatedAt": "2021-08-09T09:42:27.926Z",
            "Description": "EC2 instance i-99999999 is querying a domain "
                           "name associated with a "
                           "known Command & Control server.",
            "Id": "14bd952561ab40e0b9275f648fcca0f2",
            "Partition": "aws",
            "Region": "us-east-2",
            "Resource": {
                "InstanceDetails": {
                    "AvailabilityZone": "GeneratedFinding"
                                        "InstaceAvailabilityZone",
                    "IamInstanceProfile": {
                        "Arn": "arn:aws:iam::id:example/instance/profile",
                        "Id": "GeneratedFindingInstanceProfileId"
                    },
                    "ImageDescription": "GeneratedFinding"
                                        "InstaceImageDescription",
                    "ImageId": "ami-99999999",
                    "InstanceId": "i-99999999",
                    "InstanceState": "running",
                    "InstanceType": "c3.large",
                    "OutpostArn": "arn:aws:outposts:us-west-2:id"
                                  ":outpost/op-0fbc006e9abbc73c3",
                    "LaunchTime": "2017-12-19T01:37:35.000Z",
                    "NetworkInterfaces": [
                        {
                            "Ipv6Addresses": [],
                            "NetworkInterfaceId": "eni-bfcffe88",
                            "PrivateDnsName": "GeneratedFindingPrivateDnsName",
                            "PrivateIpAddress": "10.0.0.1",
                            "PrivateIpAddresses": [
                                {
                                    "PrivateDnsName": "Generated"
                                                      "FindingPrivateName",
                                    "PrivateIpAddress": "10.0.0.1"
                                }
                            ],
                            "PublicDnsName": "GeneratedFindingPublicDNSName",
                            "PublicIp": "198.51.100.0",
                            "SecurityGroups": [
                                {
                                    "GroupId": "Generated"
                                               "FindingSecurityId",
                                    "GroupName": "GeneratedFinding"
                                                 "SecurityGroupName"
                                }
                            ],
                            "SubnetId": "GeneratedFindingSubnetId",
                            "VpcId": "GeneratedFindingVPCId"
                        }
                    ],
                    "ProductCodes": [
                        {}
                    ],
                    "Tags": [
                        {
                            "Key": "GeneratedFindingInstaceTag1",
                            "Value": "GeneratedFindingInstaceValue1"
                        },
                        {
                            "Key": "GeneratedFindingInstaceTag2",
                            "Value": "GeneratedFindingInstaceTagValue2"
                        },
                        {
                            "Key": "GeneratedFindingInstaceTag3",
                            "Value": "GeneratedFindingInstaceTagValue3"
                        },
                        {
                            "Key": "GeneratedFindingInstaceTag4",
                            "Value": "GeneratedFindingInstaceTagValue4"
                        },
                        {
                            "Key": "GeneratedFindingInstaceTag5",
                            "Value": "GeneratedFindingInstaceTagValue5"
                        },
                        {
                            "Key": "GeneratedFindingInstaceTag6",
                            "Value": "GeneratedFindingInstaceTagValue6"
                        },
                        {
                            "Key": "GeneratedFindingInstaceTag7",
                            "Value": "GeneratedFindingInstaceTagValue7"
                        },
                        {
                            "Key": "GeneratedFindingInstaceTag8",
                            "Value": "GeneratedFindingInstaceTagValue8"
                        },
                        {
                            "Key": "GeneratedFindingInstaceTag9",
                            "Value": "GeneratedFindingInstaceTagValue9"
                        }
                    ]
                },
                "ResourceType": "Instance"
            },
            "SchemaVersion": "2.0",
            "Service": {
                "Action": {
                    "ActionType": "DNS_REQUEST",
                    "DnsRequestAction": {
                        "Domain": "GeneratedFindingDomainName"
                    }
                },
                "Evidence": {
                    "ThreatIntelligenceDetails": [
                        {
                            "ThreatListName": "GeneratedFindingThreatListName",
                            "ThreatNames": [
                                "GeneratedFindingThreatName"
                            ]
                        }
                    ]
                },
                "Archived": False,
                "Count": 3,
                "DetectorId": "detector_id",
                "EventFirstSeen": "2021-08-09T09:42:27.000Z",
                "EventLastSeen": "2021-09-20T14:24:35.000Z",
                "ResourceRole": "TARGET",
                "ServiceName": "guardduty"
            },
            "Severity": 8,
            "Title": "Command and Control server domain "
                     "name queried by EC2 instance i-99999999.",
            "Type": "Backdoor:EC2/C&CActivity.B!DNS",
            "UpdatedAt": "2021-09-20T14:24:35.130Z"
        }
    ]


def tile_data_response():
    end_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    start_time = datetime.utcfromtimestamp(
        AFFECTED_INSTANCES_CRITERIA["Criterion"]["updatedAt"]["Gt"]
    )
    start_time = start_time.strftime("%Y-%m-%dT%H:%M:%S")

    return {"data": {"cache_scope": "none",
                     "data": [{"key": 0,
                               "segments": [{"key": 0, "value": 1},
                                            {"key": 1, "value": 1}],
                               "value": 2}],
                     "hide_legend": False,
                     "label_headers": ["Affected instances", "Finding types"],
                     "labels": [["i-99999999"],
                                ["Backdoor:EC2/C&CActivity.B!DNS",
                                 "Trojan:EC2/DriveBySourceTraffic!DNS"]],
                     "observed_time": {"end_time": end_time,
                                       "start_time": start_time},
                     "valid_time": {"end_time": end_time,
                                    "start_time": start_time}}}
