#To work with regular expressions
import re
def main():
    #--Eg1. re.findall() to find patterns in a string
    text = "abc abbc ac abbbc abbbbc abbbbbbc"
    match1 = re.findall("ab.*c", text)  #*ab.c: Matches strings starting with ab, followed by any characters.i.e [.*],ending with c
    match2 = re.findall("ab*c", text)   # Matches strings starting with a, followed by 0 or more occurrences of b [b*],ending with c

    print("Matches for ab.*c:", match1)
    print("Matches for ab*c:", match2)

    #--Eg2. re.search() to find and extract a pattern
    string = "Everything is <replaced> if it's in <tags>."
    match_result = re.search("<.*?>", string)   #Searches for the first occurrence of any text between angle brackets < >, using non-greedy approach

    if match_result:
        matched_text = match_result.group()     #Returns the matched text found by re.search()
        print("Pattern found:", matched_text)
    #Output: Pattern found: <replaced>

    #--Eg3. re.sub() to replace patterns in a string
    string = "Everything is <replaced> if it's in <tags>."
    string = re.sub("<.*?>", "ELEPHANTS", string)
    print(string)  
    #Output: Everything is ELEPHANTS if it's in ELEPHANTS.
if __name__ == "__main__":
    main()