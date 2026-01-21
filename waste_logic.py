def get_explanation(waste_type):
    explanations = {
        "Wet Waste": {
            "reason": "Biodegradable organic material that decomposes naturally.",
            "disposal": "Dispose in wet waste bin or compost pit.",
            "impact": "Proper disposal reduces landfill methane emissions."
        },
        "Dry Waste": {
            "reason": "Non-biodegradable but recyclable material.",
            "disposal": "Dispose in dry/recyclable waste bin.",
            "impact": "Recycling reduces resource extraction and pollution."
        },
        "E-Waste": {
            "reason": "Contains electronic components and hazardous substances.",
            "disposal": "Dispose at authorized e-waste collection centers.",
            "impact": "Prevents toxic metal leakage into soil and water."
        },
        "Hazardous Waste": {
            "reason": "Contains chemicals that may be harmful to humans and environment.",
            "disposal": "Follow local hazardous waste disposal guidelines.",
            "impact": "Reduces risk of contamination and health hazards."
        }
    }

    return explanations.get(
        waste_type,
        {
            "reason": "Unknown waste type.",
            "disposal": "Consult local waste guidelines.",
            "impact": "Impact information unavailable."
        }
    )
