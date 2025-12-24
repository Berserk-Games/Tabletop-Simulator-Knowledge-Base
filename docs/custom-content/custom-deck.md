A custom deck is a collections of cards created via "card sheets".

![Custom Board Example](/img/custom-deck/deck.png){: style="display:block; margin:0 auto;"}

##Deck Features
* Decks can be square or rectangular, depending on dimensions of card sheet.
* Cards may be held in [hand zones](../game-tools/zone-tools.md#hand-zone) by default. This can be changed via its [context menu](../player-guides/context-menu.md#toggles).
* Multiple card sheets can be combined into larger decks if needed.
* Card sheets use the last image on a card sheet for a "hidden" image when those cards are in a hand-zone or otherwise hidden.

!!!info "See [Asset Creation](asset-creation.md) for suggested card sheet image resolution."

##Creating a Card Sheet
A deck is created from a card sheet, which is an array of images which get "cut up" into cards by the game engine. There are two methods to create these sheets, Template and Deck Builder.

###Card Sheet Template
This is the simplest way to create a card sheet. Place your card images in the relevant template and then save the resulting image. In your Steam install directory are two general-use templates for creating a card sheet.

>\Steam\steamapps\common\Tabletop Simulator\Modding\Deck Templates

???question "Can't Find Your Steam Folder?"
    * In **Steam**, go to your **Library**
    * **Right Click** on **Tabletop Simulator** and select **Properties**
    * In the Properties Menu, click **Local Files** at the top
    * Click **Browse Local Files**

![Card Sheet Template Example](/img/custom-deck/template-sheet.png){: style="display:block; margin:0 auto;"}

###Deck Builder
This tool is a little more complicated, but allows for control over the number of cards per sheet. The Deck Editor was created by **Froghut**. The Deck Builder utility is located in your game's Steam folder.

>\Steam\steamapps\common\Tabletop Simulator\Modding\Deck Builder

???question "Can't Find Your Steam Folder?"
    * In **Steam**, go to your **Library**
    * **Right Click** on **Tabletop Simulator** and select **Properties**
    * In the Properties Menu, click **Local Files** at the top
    * Click **Browse Local Files**

![Deck Editor Example](/img/custom-deck/deck-editor.png){: style="display:block; margin:0 auto;"}

* Click on **New Deck**
* Select how many cards the sheet will feature horizontally and vertically and hit **OK**
* Drag and Drop in your cards OR go to File and choose Add Cards
* Arrange the cards by drag-and-dropping them int othe desired order
    * Remember that the final card image is used as the "hidden" card face for all cards
* You can save/load these deck setups by going to File then Save Deck
* There are many other features, like background color options, view settings, etc accessible from the top menu selections
* When you are finished, go to File > Export to create the card sheet.

##Creating a Deck
Once you have a card sheet, start a Tabletop Simulator table then select **Objects > Components > Custom** to open the Custom Object menu, then select **Deck**.

!!!warning "Importing Assets"
    How you choose to import files impacts if other players can see them when you're finished.<br>For help with importing, visit [Asset Hosting](asset-importing.md).

Setting Name | Description
-- | --
Face | The path to the card sheet that will make up the face of all the cards.
Unique Backs | If each card will have its own back (in card sheet format) or if they will all share the same back image.
Back | The path to the card sheet or single card-back image.
Width | How many cards are on the card sheet (horizontal).
Height | How many cards are on the card sheet (vertical).
Number | How many cards are on the card sheet.
Sideways | Changes the ALT zoom for cards to match sideways cards.
Back is Hidden | Instead of using the last card from the card sheet as the "hidden" card, this option can use the back of the card instead.

![Deck Menu](/img/custom-deck/menu.png){: style="display:block; margin:0 auto;"}









---
