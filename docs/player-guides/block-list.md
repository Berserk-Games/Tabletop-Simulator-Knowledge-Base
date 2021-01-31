Your Block List is located in your [Configuration](/getting-started/configuration-menu) menu under the Blocked tab.

<center>![Blindfold Example](/img/block-list/block-list.png)</center>

##Blocking Players
You can add people to your list using different methods.

###As Game Host
During a game that you are host of, there are two methods to remove/avoid individuals you do not want to play with.

####Via UI
If you are the host and a disruptive player joins your server, you can click their name on the top right and click the Ban option. They will now be added to your Block List and will no longer be able to join your server, nor will you see any games they are hosting on the Server Browser.

####Via Chat
To ban a player via the chat, just type `/ban NAME`.

!!!tip "You can also type `/help` in the Game chat tab to see commands you can use via the chat."

---


###As Member
If you are joining multiplayer games but want to avoid individuals and their servers, you have a few options available.

!!!info "If someone from your block list joins a game you’re in or you join a server and someone you have blocked is in it, a warning message will pop up."

####Via Server Browser
If you right click on a server in the Server Browser, you have the option to block the host. This is good if you find offensive server names or a host you didn’t like playing with.

---


###As Either
Using Steam Name and SteamID, you can manually block any individual.

!!!tip "Locating SteamID"
    To find players’ info, go to your Steam app and click on View -> Players and view either the Current Game or Recent Games. If you remember their name, you can sort by name or by the last time you played with them. If their profile shows a username in place of numbers, you can go to any Steam ID converter to locate their Steam 64 ID.

####Via Configuration Menu
Add their name and Steam ID and  click BLOCK to your Blocked menu.

####Via JSON Edit
You can also manually add people to your Block list by editing the Blocklist.json. If you do not have a BlockList.json in your `Documents/My Games/Tabletop Simulator` folder (see also [Save Game Data Location](/getting-started/technical-info#save-game-data-location)), just create one and save it. Once you have their name and ID, open up the Blocklist.json file and input the following:

> “Name”: “Steam Name”,
“SteamID”: “123456200220000”

---
