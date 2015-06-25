from sys import stdin, stdout
import json

from pysimplesoap.client import SoapClient


__author__ = 'Lecks'

client = SoapClient(location="http://localhost:8000/")


def create(key, value):
    return client.Create(key=key, value=value).Result


def read(key):
    return client.Read(key=key).Result


def update(key, value):
    return client.Update(key=key, value=value).Result


def delete(key):
    return client.Delete(key=key).Result


def showHelp():
    print "List of commands:"
    print "1) create or c to create new object"
    print "   using: Create|c <key> <value>"
    print "   example: c foo bar"
    print
    print "2) read or r to read existing object"
    print "   using: Read|r <key>"
    print "   example: r foo"
    print
    print "3) update or u to update existing object"
    print "   using: Update|u <key> <value>"
    print "   example: u foo newBar"
    print
    print "4) delete or d for delete existing object"
    print "   using: Delete|d <key>"
    print "   example: d foo"
    print
    print "5) help or h to show help(this text)"
    print
    print "6) quit or q to exit"
    print


def showError():
    print "\033[91m" + "Invalid command" + "\033[0m"
    showHelp()

showHelp()

while True:
    stdout.write("lab3> ")
    raw = stdin.readline().rstrip('\n')
    command = raw.split()[0]
    args = raw.split()[1::]
    response = ""
    print raw

    if command == "create" or command == "c":
        response = create(args[0], args[1])

    elif command == "read" or command == "r":
        response = read(args[0])

    elif command == "update" or command == "u":
        response = update(args[0], args[1])

    elif command == "delete" or command == "d":
        response = delete(args[0])

    elif command == "help" or command == "h":
        showHelp()
        continue

    elif command == "quit" or command == "q":
        break

    if len(response) == 0:
        showError()
    else:
        print json.loads(str(response))["msg"]