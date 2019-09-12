# GrabMail

A python app grab emial attachments from different vender. Ship them to the targeted destinations. 

Setup config.json file like below:
- Mail-attach-location: The mail attachment location where all the targeted attachments saved. This is location is only relative to Mail applicaiton in Macintash.
- destination: A list of vender data and its's associated regular expression to grab the files. TODO: right now the grabing policy only applies to filenames but not the file content. 

#### config.json
```json
{
    "Mail-attach-location" : "/Users/user/Library/Mail/V*/<random code>/<mail box name>/<random code>/Data",
    "destination" : [
        {
            "name" : "<data-vender-name>",
            "reg-exp" : "^placeholder*",
            "location" : "./dir-to-go"
        }
    ]
}
```