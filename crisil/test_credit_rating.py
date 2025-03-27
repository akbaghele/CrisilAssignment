import unittest
from credit_rating import credit_rating_calculation

class TestCreditRating(unittest.TestCase):
    def test_case_1(self):
        mortgages = [
            {
                "credit_score": 750,
                "loan_amount": 200000,
                "property_value": 250000,
                "annual_income": 60000,
                "debt_amount": 20000,
                "loan_type": "fixed",
                "property_type": "single_family"
            },
            {
                "credit_score": 680,
                "loan_amount": 150000,
                "property_value": 175000,
                "annual_income": 45000,
                "debt_amount": 10000,
                "loan_type": "adjustable",
                "property_type": "condo"
            }
        ]
        self.assertEqual(credit_rating_calculation(mortgages), "AAA")

    def test_case_2(self):
        mortgages = [
            {
                "credit_score": 640,
                "loan_amount": 300000,
                "property_value": 350000,
                "annual_income": 50000,
                "debt_amount": 30000,
                "loan_type": "fixed",
                "property_type": "condo"
            },
            {
                "credit_score": 600,
                "loan_amount": 200000,
                "property_value": 250000,
                "annual_income": 40000,
                "debt_amount": 25000,
                "loan_type": "adjustable",
                "property_type": "single_family"
            }
        ]
        self.assertEqual(credit_rating_calculation(mortgages), "C")

    def test_case_3(self):
        mortgages = [
            {
                "credit_score": 720,
                "loan_amount": 250000,
                "property_value": 300000,
                "annual_income": 80000,
                "debt_amount": 15000,
                "loan_type": "fixed",
                "property_type": "single_family"
            },
            {
                "credit_score": 690,
                "loan_amount": 180000,
                "property_value": 200000,
                "annual_income": 60000,
                "debt_amount": 20000,
                "loan_type": "fixed",
                "property_type": "condo"
            }
        ]
        self.assertEqual(credit_rating_calculation(mortgages), "BBB")

if __name__ == '__main__':
    unittest.main()