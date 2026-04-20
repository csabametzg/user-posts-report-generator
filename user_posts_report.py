import requests
import json
import csv


def get_users_data():

    users_url = "https://jsonplaceholder.typicode.com/users"

    users_api_data = None

    try:
        with requests.Session() as session:
            # 1. Attempt the request
            response = session.get(users_url, timeout=5)
            print("OK | Users - Attempt the request")

            # Get latency in seconds or milliseconds
            latency_seconds = response.elapsed.total_seconds()
            print(f"OK | Users - HTTP Latency: {latency_seconds * 1000:.2f} ms")


            # 2. Raise an exception for 4xx or 5xx HTTP status code
            response.raise_for_status()
            print("OK | Users - Raise an exception for 4xx or 5xx HTTP status code")


            # 3. Process the JSON if successful
            if 'application/json' in response.headers.get('Content-Type', ''):
                users_api_data = response.json()
                print("OK | Users - Process the JSON if successful")
            else:
                raise ValueError("Error | Users: The server returned a non-JSON response.")


    except requests.exceptions.HTTPError as http_err:
        # Catches 404, 500, etc.
        print(f"Users | HTTP error occurred: {http_err}")

    except requests.exceptions.ConnectionError:
        # Catches network issues or wrong URLs
        print("Users | Could not connect to the server.")

    except requests.exceptions.Timeout:
        # Catches requests that take too Long
        print("Users | Error: The request timed out.")

    except requests.exceptions.RequestException as err:
        # Generic catch-all for any other requests-related issues
        print(f"Users | An unexpected error occured: {err}")

    except ValueError:
        # If the API returns malformed JSON, response.json() will raise a ValueError.
        print("Users | Failed to parse JSON response.")


    finally:
        # Always runs, regardless of success of failure
        print("OK | Users - API request attempt finished.")

        # Process data outside the error handling
        if users_api_data:
            print(f"\nSuccessfully retrieved {len(users_api_data)} users.\n")

    return users_api_data




def get_posts_data():
    posts_url = "https://jsonplaceholder.typicode.com/posts"

    posts_api_data = None

    try:
        with requests.Session() as session:
            # 1. Attempt the request
            response = session.get(posts_url, timeout=5)
            print("OK | Posts - Attempt the request")

            # Get latency in seconds or milliseconds
            latency_seconds = response.elapsed.total_seconds()
            print(f"OK | Posts - HTTP Latency: {latency_seconds * 1000:.2f} ms")

            # 2. Raise an exception for 4xx or 5xx HTTP status code
            response.raise_for_status()
            print("OK | Posts - Raise an exception for 4xx or 5xx HTTP status code")

            # 3. Process the JSON if successful
            if 'application/json' in response.headers.get('Content-Type', ''):
                posts_api_data = response.json()
                print("OK | Posts - Process the JSON if successful")
            else:
                raise ValueError("Error | Posts: The server returned a non-JSON response.")


    except requests.exceptions.HTTPError as http_err:
        # Catches 404, 500, etc.
        print(f"Posts | HTTP error occurred: {http_err}")

    except requests.exceptions.ConnectionError:
        # Catches network issues or wrong URLs
        print("Posts | Could not connect to the server.")

    except requests.exceptions.Timeout:
        # Catches requests that take too Long
        print("Posts | Error: The request timed out.")

    except requests.exceptions.RequestException as err:
        # Generic catch-all for any other requests-related issues
        print(f"Posts | An unexpected error occured: {err}")

    except ValueError:
        # If the API returns malformed JSON, response.json() will raise a ValueError.
        print("Posts | Failed to parse JSON response.")


    finally:
        # Always runs, regardless of success of failure
        print("OK | Posts - API request attempt finished.")

        # Process data outside the error handling
        if posts_api_data:
            print(f"\nSuccessfully retrieved {len(posts_api_data)} posts.\n")

    return posts_api_data




def json_connect_data(users_data, posts_data, user_id):

    data = {}

    post_count = 0
    first_post_title = None

    for user in users_data:
        if user['id'] == user_id:
            data["user_id"] = user['id']
            data['username']= user['name']

    if "username" not in data:
        print("No such user exists.")
        return None



    for post in posts_data:
        if post['userId'] == user_id:
            post_count += 1

            if post_count == 1:
                first_post_title = post['title']

            data["post_count"] = post_count


    if first_post_title is None:
        data["first_post_title"] = "N/A"
    else:
        data["first_post_title"] = first_post_title


    return data




def save_to_json(data, filename):

    with open(filename, mode="w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)



def save_to_txt(data, filename):
    with open(filename, mode="w", encoding="utf-8") as txt_file:
            txt_file.write(f"User ID: {data['user_id']}\nUsername: {data['username']}\nPost count: {data['post_count']}\nFirst post title: {data['first_post_title']}")



def save_to_csv(data, filename):
    with open(filename, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data.keys())

        writer.writeheader()
        writer.writerow(data)



def main():
    while True:
        try:
            user_id = int(input("Please enter a user ID number:\n"))
            break
        except ValueError:
            print("Invalid input, enter a number.")


    filename_json = "report.json"
    filename_txt = "report.txt"
    filename_csv = "report.csv"


    users_data = get_users_data()
    posts_data = get_posts_data()

    if users_data is None or posts_data is None:
        print("PI error, please try again.")
        return

    result_json = json_connect_data(users_data, posts_data, user_id)

    if result_json:
        print(result_json)

        save_to_json(result_json, filename_json)
        save_to_txt(result_json, filename_txt)
        save_to_csv(result_json, filename_csv)

        print("3 files saved successfully.")



if __name__ == "__main__":
    main()



