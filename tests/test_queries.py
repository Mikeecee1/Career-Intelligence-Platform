from pprint import pprint
from src.database.query import *

print(f"Total jobs: {total_jobs()}")

print("\nTop employers")
pprint(top_employers())

print("\nTop locations")
pprint(top_locations())


# print("\nJobs by contract")
# pprint(jobs_by_contract_type())

print("\nSalary statistics")
pprint(salary_statistics())

print("\nSearch for nurse")
pprint(search_job_title("nurse")[:5])