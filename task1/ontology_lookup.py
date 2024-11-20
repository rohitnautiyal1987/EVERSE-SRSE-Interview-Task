import requests
import sys

def fetch_ontology_details(ontology_id):
    # Function to fetch ontology details from 
    #  # Send a GET request to the APIAPI
    url = f"https://www.ebi.ac.uk/ols/api/ontologies/{ontology_id}"
    print(f"Fetching details for ontology ID: {ontology_id}")  # Debug
    #print(f"Fetching details for ontology ID:")  # Debug

    try:
        # Send a GET request to the API
        response = requests.get(url)
        # print("Response status code111:"+response.text)  # Debug
        response.raise_for_status()  # Check if the request was successful

         # Parse the JSON response
        data = response.json()
        ontology_info = {
            "Title": data.get("config", {}).get("title", "N/A"),
            "Description": data.get("config", {}).get("description", "N/A"),
            "Number of Terms": data.get("numberOfTerms", "N/A"),
            "Status": data.get("status", "N/A")
        }
        print("Fetched ontology details successfully.")  # Debug
        return ontology_info

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Debug
        return {"Error": f"HTTP error occurred: {http_err}"}
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")  # Debug
        return {"Error": f"Error connecting to the API: {req_err}"}
    except Exception as e:
        print(f"An error occurred: {e}")  # Debug
        return {"Error": f"An error occurred: {e}"}
    pass
    # Function to print ontology details
def print_ontology_info(ontology_id):
    details = fetch_ontology_details(ontology_id)

    if "Error" in details:
        print(details["Error"])
    else:
    # Print ontology details
        print("Ontology Details:")
        print(f"Title: {details['Title']}")
        print(f"Description: {details['Description']}")
        print(f"Number of Terms: {details['Number of Terms']}")
        # print(f"Status: {details['Status']}")
        print(f"Status: {details['Status']}")
# Entry point for running the script directly
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ontology_lookup.py <ontology_id>")
        sys.exit(1)

    ontology_id = sys.argv[1]
    print(f"Received ontology ID: {ontology_id}")  # Debug
    print_ontology_info(ontology_id)
    pass

def main():
    if len(sys.argv) != 2:
        print("Usage: ontology-lookup <ontology_id>")
        sys.exit(1)
    ontology_id = sys.argv[1]
    print_ontology_info(ontology_id)

if __name__ == "__main__":
    main()
