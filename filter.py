class ParseWebRequest:

    def __init__(self, requestsFile):
        self.headers = {}
        self.request = requestsFile
        self.RequestType = ""

    def dictionary_convert(self, headerDictionary, line, end_of_line):
        separatorPassed = 0
        # Fix I came up w/ in case there was more than one  colon ':' character, if we already passed it just skip
        for c in range(0, end_of_line):
            # Iterate through the first -> last character of a line
            if line[c] == ':' and separatorPassed == 0:
                # ':' is a separator in the file
                header_name = ""
                header_value = ""
                separatorPassed = 1
                for i in range(0, c):
                    # From first character of line to ':' identified, add that to header name
                    header_name = header_name + line[i]
                # From point after ':' symbol "+2" to end of file add to header value
                for j in range(c + 2, end_of_line):
                    header_value = header_value + line[j]
                    headerDictionary[header_name] = header_value
                # Pushes header value & name to dictionaries

    def cookie_categorize(self, headerDictionary, line):
        cookie_header = "Cookie"
        cookie_value = ''
        for k in range(8, len(line) - 1):
            cookie_value = cookie_value + line[k]
        headerDictionary[cookie_header] = cookie_value

    def data_convert(self, dataDictionary, line, end_of_line):
        name = 1
        data_name = ""
        data_value = ""

        for l in range(0, end_of_line):
            if line[l] == "=":
                name = 0

            elif line[l] == "&":
                dataDictionary[data_name] = data_value
                data_name = ""
                data_value = ""
                name = 1

            elif name == 1:
                data_name = data_name + line[l]
            else:
                data_value = data_value + line[l]

        dataDictionary[data_name] = data_value

    def parseRequest(self):
        f = open(self.request, "r")
        for line in f:
            eol = len(line) - 1
            if "POST " in line:
                self.RequestType = "POST" # print("Identified POST Request")
            elif "GET " in line:
                self.RequestType = "GET"
            elif "Cookie: " in line:
                # Filtering lines with cookies
                self.cookie_categorize(self.headers, line, )

            elif ": " in line:
                self.dictionary_convert(self.headers, line, eol)
        f.close()
