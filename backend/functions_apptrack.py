from flask import Flask, request, url_for, session, redirect
import os
from simplegmail import Gmail
from simplegmail.query import construct_query
from simplegmail.query import _read

gmail = Gmail()

# To get the unread messages from the inbox
def get_unread_inbox():
    unread_inbox = gmail.get_unread_inbox()
    for message in unread_inbox:
        print("\nFrom: " + message.sender)
        print("Subject: " + message.subject)
        print("Date: " + message.date)
        print("Body: " + message.plain)
    
    return unread_inbox

# To get the read messages from the inbox
def get_read_updates():
    read_updates_query_params = {
        "labels":[["Inbox"]],
        "read": True
    }
    read_updates = gmail.get_messages(query=construct_query(read_updates_query_params))

    for message in read_updates:
        print("\nFrom: " + message.sender)
        print("Subject: " + message.subject)
        print("Date: " + message.date)
        print("Body: " + message.plain)
    
    return read_updates


# To get the unread messages from the Updates section, set Label to "Updates"
def get_unread_updates():
    unread_updates_query_params = {
        "labels":[["Updates"]]
    }
    unread_updates = gmail.get_unread_messages(query=construct_query(unread_updates_query_params))

    for message in unread_updates:
        print("\nFrom: " + message.sender)
        print("Subject: " + message.subject)
        print("Date: " + message.date)
        print("Body: " + message.plain)
    
    return unread_updates

# To get read messages from the Updates section, set Label to "Updates". Then, query where unread is False
def get_read_updates():
    read_updates_query_params = {
        "labels":[["Updates"]],
        "read": True
    }
    read_updates = gmail.get_messages(query=construct_query(read_updates_query_params))

    for message in read_updates:
        print("\nFrom: " + message.sender)
        print("Subject: " + message.subject)
        print("Date: " + message.date)
        print("Body: " + message.plain)
    
    return read_updates

"""
To get read messages with an exact phrase, use "exact_phrase" in the query parameters.
Each phrase in a comma separated list within "exact_phrases=()" will 'and' them and give you messages with all phrases.
To do or, query as shown below:
construct_query(
    {exact_phrases=()},
    {exact_phrases=()},
    ...
    )
Alternatively, feel free to store each query in some variable and use the variables as your parameters
    
"""
# exact_phrase_query_params = {
#     exact_phrase=()
# }
construct_query()
