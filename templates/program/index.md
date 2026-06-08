<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Speaker Schedule</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: #f9fafb;
            color: #1f2937;
            padding: 2rem;
        }

        .program-table {
            width: 100%;
            max-width: 900px;
            margin: 0 auto;
            border-collapse: collapse;
            background: #ffffff;
            border-radius: 8px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }

        th {
            background-color: #f3f4f6;
            color: #4b5563;
            text-align: left;
            padding: 1rem;
            font-weight: 600;
            border-bottom: 2px solid #e5e7eb;
        }

        .speaker-row {
            cursor: pointer;
            transition: background-color 0.2s ease;
            border-bottom: 1px solid #e5e7eb;
        }

        .speaker-row:hover {
            background-color: #f8fafc;
        }

        .speaker-name {
            color: #2563eb;
            font-weight: 600;
            text-decoration: underline;
        }

        .talk-title {
            font-weight: 500;
            padding: 1rem;
        }

        .padding-cell {
            padding: 1rem;
        }

        /* Hidden detail drawer styling */
        .details-row {
            display: none;
            background-color: #f8fafc;
            border-bottom: 1px solid #e5e7eb;
        }

        .details-container {
            padding: 1.5rem;
            font-size: 0.95rem;
            line-height: 1.6;
            color: #374151;
        }

        .details-section {
            margin-bottom: 1rem;
        }

        .details-section strong {
            color: #111827;
            display: block;
            margin-bottom: 0.25rem;
            text-transform: uppercase;
            font-size: 0.8rem;
            letter-spacing: 0.05em;
        }
    </style>
</head>
<body>
    <table class="program-table">
        <thead>
            <tr>
                <th style="width: 25%;">Speaker</th>
                <th style="width: 75%;">Presentation Title</th>
            </tr>
        </thead>
        <tbody>
            
            <!-- Trevor Cohen's Main Row -->
            <tr class="speaker-row" onclick="toggleBio('cohen-details')">
                <td class="padding-cell">
                    <span class="speaker-name">Trevor Cohen</span>
                </td>
                <td class="talk-title">
                    Linguistic Indicators of Symptom Severity in Mental Health: From Lexicons to Large Language Models
                </td>
            </tr>

            <!-- Expandable Bio & Abstract Drawer -->
            <tr id="cohen-details" class="details-row">
                <td colspan="2">
                    <div class="details-container">
                        <div class="details-section">
                            <strong>Abstract</strong>
                            Language is the medium through which both assessment and therapy are conducted in the care of mental health conditions. The rapid advancement of natural language processing (NLP) technologies presents new avenues for automated appraisal of patient-generated language to support care delivery. This talk will provide an overview of an extended program of research focused on automated appraisal of language across a range of mental health conditions - from assessment of speech in psychosis through detection of suicide risk in internet search logs - with a focus on the relationship between the constraints and capabilities of evolving NLP technologies, and their utility in characterizing the linguistic manifestations of mental health conditions.
                        </div>
                        <div class="details-section" style="margin-bottom: 0;">
                            <strong>Bio</strong>
                            Dr. Cohen trained and practiced as a physician in South Africa before earning a PhD in Biomedical Informatics from Columbia University in 2007. His doctoral research focused on improving understanding of psychiatric clinical text using computational models language. He later held faculty positions at Arizona State University and the University of Texas School of Biomedical Informatics, where he worked on representing and applying knowledge extracted from the biomedical literature, amongst other research topics. Since joining the University of Washington in 2018, his work has focused on detecting linguistic indicators of neurocognitive and mental health status, summarizing biomedical literature in plain language, and addressing sources of inaccuracy in clinical language models. Dr. Cohen’s work has been supported by the National Library of Medicine and the National Institute of Mental Health, amongst other sources. He is a Fellow of the American College of Medical Informatics, lead editor of a textbook on AI in medicine, and co-author of a recent book on large language models.
                        </div>
                    </div>
                </td>
            </tr>
            <!-- You can add other speaker rows here following the same pattern -->
        </tbody>
    </table>

    <script>
        function toggleBio(rowId) {
            const detailRow = document.getElementById(rowId);
            if (detailRow.style.display === "table-row") {
                detailRow.style.display = "none";
            } else {
                detailRow.style.display = "table-row";
            }
        }
    </script>

</body>
</html>
