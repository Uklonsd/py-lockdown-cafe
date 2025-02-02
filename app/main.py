from app.cafe import Cafe
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


def go_to_cafe(friends: list, cafe: str) -> str:
    masks_needed = 0
    try:
        for friend in friends:
            try:
                cafe.visit_cafe(friend)
            except NotVaccinatedError:
                return "All friends should be vaccinated"
            except OutdatedVaccineError:
                return "All friends should be vaccinated"
            except NotWearingMaskError:
                masks_needed += 1
        if masks_needed > 0:
            return f"Friends should buy {masks_needed} masks"
        return f"Friends can go to {cafe.name}"
    except Exception as e:
        return str(e)


if __name__ == "__main__":
    import datetime

    friends = [
        {
            "name": "Alisa",
            "vaccine": {
                "expiration_date": datetime.date.today()
            },
            "wearing_a_mask": True
        },
        {
            "name": "Bob",
            "vaccine": {
                "expiration_date": datetime.date.today()
            },
            "wearing_a_mask": True
        },
    ]

    cafe = Cafe("KFC")
    print(go_to_cafe(friends, cafe))
