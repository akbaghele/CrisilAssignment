def credit_rating_calculation(mortgage_list):
    overall_risk_score = 0
    credit_scores = []

    for mortgage in mortgage_list:
        individual_risk_score = 0
        borrower_credit_score = mortgage['credit_score']
        credit_scores.append(borrower_credit_score)

        # Calculate Loan-to-Value (LTV) Ratio
        ltv_ratio = mortgage['loan_amount'] / mortgage['property_value']
        if ltv_ratio > 0.9:
            individual_risk_score += 2
        elif ltv_ratio > 0.8:
            individual_risk_score += 1

        # Calculate Debt-to-Income (DTI) Ratio
        dti_ratio = mortgage['debt_amount'] / mortgage['annual_income']
        if dti_ratio > 0.5:
            individual_risk_score += 2
        elif dti_ratio > 0.4:
            individual_risk_score += 1

        # Impact of Credit Score
        if borrower_credit_score >= 700:
            individual_risk_score -= 1
        elif borrower_credit_score < 650:
            individual_risk_score += 1

        # Loan Type Influence
        if mortgage['loan_type'] == "adjustable":
            individual_risk_score += 1
        else:  # fixed
            individual_risk_score -= 1

        # Property Type Influence
        if mortgage['property_type'] == "condo":
            individual_risk_score += 1

        overall_risk_score += individual_risk_score

    # Adjust based on Average Credit Score
    avg_credit_score = sum(credit_scores) / len(credit_scores)
    if avg_credit_score >= 700:
        overall_risk_score -= 1
    elif avg_credit_score < 650:
        overall_risk_score += 1

    # Determine Final Credit Rating
    if overall_risk_score <= 2:
        return "AAA"
    elif 3 <= overall_risk_score <= 5:
        return "BBB"
    else:
        return "C"