import sys

sys.path.append("src")

from ai.planner_service import PlannerService
from models.lead import Lead


lead = Lead(
    name="Rahul Sharma",
    phone="9876543210",
    email="rahul@gmail.com",
    company="ABC Pvt Ltd",
    business_type="Retail",
    city="Delhi",
    notes="Interested in payment solutions",
)

service = PlannerService()

plan = service.generate_plan(
    lead,
    "HIGH",
)

print(plan)