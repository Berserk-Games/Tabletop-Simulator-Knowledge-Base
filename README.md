# Tabletop Simulator Knowledge Base

This is the source of the knowledge base in Tabletop Simulator. It uses a modified version of [Material-Design](https://github.com/squidfunk/mkdocs-material) for MKDocs.

## How it Works

The `.md` files in the `/docs` folder are written in Markdown, which is an easy-to-use markup language to add formatting to text. Additionally, some custom CSS is used, as well as a handful of custom images. When making changes, it is possible to live-preview them as you go if you have set up the local files for mkdocs + material design.

Alternatively, you can make modifications to individual pages then submit them for review. The developers will always be the ones to build and publish the site anyway, all you will do is modify the contents of this Git.

### Installing

If you choose to install MKDocs so you can live-preview your changes, you may do so [by following these instructions](https://squidfunk.github.io/mkdocs-material/getting-started/).

Otherwise, you will not need to install anything to edit the text files.


#### Steps

* Have a working `pipenv`
* In this folder, do `pipenv install`.  You might need elevated priviledges.
* `pipenv shell`
* `pip install mkdocs`
* `pip install pymdown-extensions `
* `pip install mkdocs-material==4.6.3`

* `mkdocs build` to build the docs
* `mkdocs serve` to run the docs on a local webserver for testing.
* `mkdocs gh-deploy` to deploy
