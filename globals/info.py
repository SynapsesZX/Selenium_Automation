import page_objects.base_page
from page_objects.base_page import BasePage
from requests.auth import HTTPBasicAuth
from dataclasses import dataclass

bearer = {
    "Authorization": "eyJraWQiOiIreEc3T0Zlc0pkamRLOW5USStCN1plVmc4MUt2U1hRSisycFoxZTZYckZvPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI2OWM0YTUyMC1kNDgxLTQ0ZWQtOWMxOS04ODhiZTU0NTFhNWUiLCJjb2duaXRvOmdyb3VwcyI6WyJEZXZlbG9wZXIiXSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLXdlc3QtMi5hbWF6b25hd3MuY29tXC91cy13ZXN0LTJfWFpnN0RISDRkIiwidmVyc2lvbiI6MiwiY2xpZW50X2lkIjoiNDRiZGVyNG1jOGo1ZG8xbjYwaGhwb2tpZW8iLCJvcmlnaW5fanRpIjoiOTNhNWQ1MDgtMGNlMy00MWM0LWIwN2UtMGNkNWJlYzJmZGE4IiwiZXZlbnRfaWQiOiJjMmRjNzExNS01YzZhLTQ2YmEtYTk1Mi0yZTQ2ODg3MDk4NjUiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6Im9wZW5pZCIsImF1dGhfdGltZSI6MTY2Mjk3NTg5NSwiZXhwIjoxNjYzMDYyMjk1LCJpYXQiOjE2NjI5NzU4OTUsImp0aSI6ImMxNTc1NGViLWRhZjEtNGZlMS1iY2RjLTc0NzI4ZjY2OTE2NSIsInVzZXJuYW1lIjoiaWdvciJ9.Jr-J0v1xEZZ3k25AvNH78xHVWevx77sP0ohGmmzHUaFT9qhdLezboC6MyAlisCGayzPYJk9MWOOiREhPkZwKwYlsdA5De1LiFhdgFB2G4z4DJ5ZyqdLOuQi5jVwbJC66v8L5AnGCIsVKuscYtZzLtrREWJbe9k_dvxX_acv8_XWDW-7N705g5POmM9gQjUf2Zan7rb3wFdPskKogzpd1yb7J_5KU8yLrdKaocHMcgpGFj4kVqyGCGDVZlcNDaWo_b8_Ult0mPowkUJCPzUp4cKRY_3k5aQJ-yXZm1xbyVVoxaou9BI-FbEqzNJHOlsiS4kZfqQdutd7-Y-FygbNmLw"}
admin_bearer = {
    'Authorization': "eyJraWQiOiIreEc3T0Zlc0pkamRLOW5USStCN1plVmc4MUt2U1hRSisycFoxZTZYckZvPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI4ZGM2MGI4NC1jNjMxLTQzZjItOTI3NS1iOTRmNjdlOTdjZjkiLCJjb2duaXRvOmdyb3VwcyI6WyJBZG1pbiJdLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtd2VzdC0yLmFtYXpvbmF3cy5jb21cL3VzLXdlc3QtMl9YWmc3REhINGQiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiI3ZDFmbGFiMDExZTZndTEzOHVocXAwbTRxMCIsIm9yaWdpbl9qdGkiOiI2ODFkMDkwMS0zMmFiLTQ3MTItOGNiMy01ZWQ3OTEzNDFjYjQiLCJldmVudF9pZCI6ImY1NGJlMWVjLWE5Y2EtNGFhNy04MWM2LTIwZDc1M2VmODdiYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoib3BlbmlkIiwiYXV0aF90aW1lIjoxNjY5MDExNTY5LCJleHAiOjE2NjkwOTc5NjksImlhdCI6MTY2OTAxMTU2OSwianRpIjoiZGJlMzI2NWYtODg5Yi00ZjMzLWJhMjktYzgzN2QxZmYyYWVmIiwidXNlcm5hbWUiOiJodW1hbiJ9.xl0yLDXEYqTdUAFQ_i_WOQqTH2iZdiorTCa2hBMroQeaRA0y9Jg51jVM0ud6iBSlWcwl4jKMpMUu3c4NFsgVrLFmpyg_CIWDF9kiD6jkpL02Fm5QdMlUol2_6eMB6_XhONewcZ4jKNfPu5A_lZaJeZtL5l4jk_E3ssN42O2ful1xy3Cj5GObhv_jc2kNQREgwSRfUAx5tBAs9G_cKgqHcWTEVaeMe-BcppuyeNg1yYYwZiFxjww2oGCAnAE0JKfrkS2T6qwqSvArhuYlRhQnuR9Ziq6jep2tBOL3j_hXdYzFVyI4RCFzf-_MOZZaqoVeTXvh6vsft3NkRxDs_uoZPw"}
user_login = 'igorzyabrov2050@gmail.com'
user_password = 'I771948741infqy!'
admin_login = 'human360dev@gmail.com'
admin_password = 'I771948741infqy!'
scopes_for_individual_patient = ['AllergyIntolerance', 'Appointment', 'Binary', 'CarePlan', 'CareTeam', 'Condition',
                                 'Consent', 'Coverage', 'Device', 'DiagnosticReport', 'DocumentReference', 'Encounter',
                                 'Goal', 'Immunization', 'Medication', 'MedicationRequest', 'Observation',
                                 'Organization', 'Patient', 'Practitioner', 'PractitionerRole', 'Procedure',
                                 'Provenance', 'RelatedPerson', 'ServiceRequest']
country_list = ['Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica',
                'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
                'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan',
                'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina',
                'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam',
                'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Cayman Islands',
                'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands',
                'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica',
                'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czechia', "Côte d'Ivoire", 'Denmark', 'Djibouti', 'Dominica',
                'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia',
                'Eswatini', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France',
                'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia',
                'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala',
                'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands',
                'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia',
                'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan',
                'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of",
                'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon',
                'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Madagascar',
                'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania',
                'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco',
                'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal',
                'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue',
                'Norfolk Island', 'North Macedonia', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau',
                'Palestine, State of', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn',
                'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Romania', 'Russian Federation', 'Rwanda', 'Réunion',
                'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis',
                'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon',
                'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia',
                'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia',
                'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa',
                'South Georgia and the South Sandwich Islands', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan',
                'Suriname', 'Svalbard and Jan Mayen', 'Sweden', 'Switzerland', 'Syrian Arab Republic',
                'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste',
                'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan',
                'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom',
                'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu',
                'Venezuela, Bolivarian Republic of', 'Viet Nam', 'Virgin Islands, British', 'Virgin Islands, U.S.',
                'Wallis and Futuna', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe', 'Åland Islands']
canada_states = ['Alberta', 'British Columbia', 'Manitoba', 'New Brunswick', 'Newfoundland and Labrador',
                 'Northwest Territories', 'Nova Scotia', 'Nunavut', 'Ontario', 'Prince Edward Island', 'Quebec',
                 'Saskatchewan', 'Yukon']
india_states = ['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunāchal Pradesh', 'Assam', 'Bihār', 'Chandīgarh',
                'Chhattīsgarh', 'Delhi', 'Dādra and Nagar Haveli and Damān and Diu', 'Goa', 'Gujarāt', 'Haryāna',
                'Himāchal Pradesh', 'Jammu and Kashmīr', 'Jhārkhand', 'Karnātaka', 'Kerala', 'Ladākh', 'Lakshadweep',
                'Madhya Pradesh', 'Mahārāshtra', 'Manipur', 'Meghālaya', 'Mizoram', 'Nāgāland', 'Odisha', 'Puducherry',
                'Punjab', 'Rājasthān', 'Sikkim', 'Tamil Nādu', 'Telangāna', 'Tripura', 'Uttar Pradesh', 'Uttarākhand',
                'West Bengal']
united_states = ['Alabama', 'Alaska', 'American Samoa', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut',
                 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Guam', 'Hawaii', 'Idaho', 'Illinois',
                 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan',
                 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
                 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Northern Mariana Islands', 'Ohio',
                 'Oklahoma', 'Oregon', 'Pennsylvania', 'Puerto Rico', 'Rhode Island', 'South Carolina', 'South Dakota',
                 'Tennessee', 'Texas', 'United States Minor Outlying Islands', 'Utah', 'Vermont',
                 'Virgin Islands, U.S.', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
category_id = BasePage.random_with_N_digits(5)
category_name = BasePage.randomWord(10)
valid_url = 'https://www.google.com/'
pet_api_key = HTTPBasicAuth('apikey', 'special-key')



