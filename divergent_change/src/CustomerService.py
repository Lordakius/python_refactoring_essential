import re

class CustomerService:
    def is_valid_email(self, email: str) -> bool:
        return EmailValidator.is_valid_email(self, email)

    def format_display_name(self, first_name: str, last_name: str) -> str:
        return CustomerDisplayFormatter.format_display_name(self, first_name, last_name)

    def calculate_loyalty_points(self, number_of_purchases: int) -> int:
        return LoyaltyService.calculate_loyalty_points(self, number_of_purchases)

    def determine_account_status(self, days_since_last_login: int) -> str:
        return AccountStatusService.determine_account_status(self, days_since_last_login)

class EmailValidator:

    def is_valid_email(self, email: str) -> bool:
        if email is None:
            return False
        pattern = r"^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$"
        return re.match(pattern, email) is not None

class CustomerDisplayFormatter:

    def format_display_name(self, first_name: str, last_name: str) -> str:
        return f"{first_name.strip()} {last_name.strip().upper()}"

class LoyaltyService:

    def calculate_loyalty_points(self, number_of_purchases: int) -> int:
        return number_of_purchases * 10

class AccountStatusService:

    def determine_account_status(self, days_since_last_login: int) -> str:
        if days_since_last_login > 365:
            return "INACTIVE"
        elif days_since_last_login > 30:
            return "DORMANT"
        return "ACTIVE"
