import os
import requests
import markdown2

def update_canvas_page(url, page_name):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for errors in the HTTP request

        # Convert Markdown to HTML
        html_content = markdown2.markdown(response.text, extras=["fenced-code-blocks"])
        html_content = html_content.replace('<code>', '<code style="font-size: 20px;">')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the file: {e}")
        return

    token = os.getenv("CANVAS_API_TOKEN")
    course_id = os.getenv("CANVAS_COURSE_ID")
    page_url = f"https://canvas.instructure.com/courses/{course_id}/pages/{page_name}"
    canvas_url = "https://canvas.instructure.com"

    # API endpoint to update the contents of a page
    api_endpoint = f"{canvas_url}/api/v1/courses/{course_id}/pages/{page_name}"

    # Set up the request headers with the Authorization token
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    # Make the request to the Canvas API to get the current page content
    response_get = requests.get(api_endpoint, headers=headers)

    content = html_content

    # Check if the request was successful (status code 200)
    if response_get.status_code == 200:
        # Parse the response JSON data
        data = response_get.json()

        # Update the content in the page
        updated_content = {
            "wiki_page": {
                "body": content,  # Replace with your updated content
            }
        }

        # Make the PUT request to update the page content
        response_put = requests.put(api_endpoint, headers=headers, json=updated_content)

        # Check if the update was successful (status code 200)
        if response_put.status_code == 200:
            print("Page content updated successfully.")
        else:
            print(f"Error updating page content: {response_put.status_code} - {response_put.text}")
    else:
        # Print an error message if the initial request was not successful
        print(f"Error: {response_get.status_code} - {response_get.text}")

# Example usage:
if __name__ == "__main__":
    url_input = "https://raw.githubusercontent.com/ChpcTraining/css2024_notes/refs/heads/main/week1/day4_dara/astropy.md"
    page_name_input = "4-astropy"
    update_canvas_page(url_input, page_name_input)

