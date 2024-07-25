#!/usr/bin/env python

"""This is just an example of using the summary library, such as how you would call it from a python notebook. """

#!/usr/bin/env python

from collections import defaultdict
from pathlib import Path
from ncpi_fhir_client.fhir_client import FhirClient
from ncpi_fhir_client.host_config import get_host_config
from summary.report_fhir_counts import summarize_study, AVAILABLE_STUDIES
import yaml


def exec():
    # This will read the contents of the local file, fhir_hosts where the different
    # FHIR servers are configured. This file MUST NOT be checked into GITHUB since
    # it will likely house your API secrets.
    host_config = get_host_config()

    # We have to instantiate our host. I recommend having two entries in your
    # fhir_hosts file: QA and PROD

    for environ in ["QA", "PROD"]:
        # Dump the summary to file
        report_path = Path("output") / "summary" / environ
        # We'll make sure the directory does exist before trying to write to it
        report_path.mkdir(parents=True, exist_ok=True)

        server_summaries = {}
        fhir_client = FhirClient(host_config[environ])

        print(f"FHIR Server: {fhir_client.target_service_url}")

        for study in AVAILABLE_STUDIES:
            print(f"-------------------{study}--------------------")

            server_summaries[study] = summarize_study(fhir_client, study)

            # Do stuff with a given study's summary info
            # For this, we'll just write the results to a file named after the
            # study inside the appropriate directory

            # Because the defaultdict seems to be overly complex for YAML to handle,
            # we have to strip it down to a very basic dictionary. There is probaby
            # some way to clarify to it that we don't want to treat those differently,
            # but time is too limited ATM:

            # print(summary)
            # pdb.set_trace()
            final_report = {}
            for key, value in server_summaries[study].items():
                if type(value) is defaultdict:
                    final_report[key] = {}

                    for subkey in value:
                        if type(value[subkey]) is defaultdict:
                            if subkey not in final_report[key]:
                                final_report[key][subkey] = {}
                            for subsubkey in value[subkey]:
                                final_report[key][subkey][subsubkey] = value[subkey][
                                    subsubkey
                                ]
                        else:
                            final_report[key][subkey] = value[subkey]

                else:
                    final_report[key] = value

            report_filename = report_path / f"fhir_summary_{study}.yaml"
            with report_filename.open("wt") as f:
                yaml.dump(final_report, f)
                print(yaml.dump(final_report))


if __name__ == "__main__":
    exec()
