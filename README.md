# Cohen Lab website

[https://bclab.wustl.edu/](https://bclab.wustl.edu/)

This repository contains the files and content for the Cohen Lab website. The website is built as a static site generated from the content in this repository using [Zola](https://getzola.org).

Pushing a commit to this repository will automatically trigger a website build, and the rendered website content will be committed to the `gh-pages` branch. Avoid making edits to the the `gh-pages` branch directly, as they will be overwritten upon the next push to `main`.

# Editing Content

In general, if you would like to make or edit a blog post, or modify any of the website page content, you only need to look in the `content` directory. In Zola sites, each page of the website is represented by either a single [Markdown](https://commonmark.org/) (`.md`) file or a folder containing a Markdown file named `index.md` or `_index.md`\*. For instance, if you wanted to edit the research area page on MPRAs, you would edit `content/research/MPRAs.md`. If you wanted to edit the research overview page, you would edit `content/research/_index.md`.

## File Size Notice

**Please try to avoid uploading any large images or attachments (>10 MB)**. They make the git repository slow, and there are caps on the size of GitHub repositories, individual version-controlled files, and GitHub Pages websites. If you must reference a large photo or attachment, host it on WUStL Box, and reference it with a hyperlink.

## Writing Blog Posts

### Without Images/Attachments

To create a new blog post without any images or attachments, create a new Markdown file in the `content/posts` folder. The file name should be of the format `YYYY-MM-DD-[short-descriptor].md`. `YYYY-MM-DD` will be parsed to retrieve the post date, and `[short-descriptor]` will become the post URL (e.g. `/posts/short-descriptor`). In the Markdown file, enter the following:

```
+++
title = "Your Post Title"
[taxonomies]
authors=["You"]
tags=["tag1", "tag2"]
+++
```

Look at the existing website to see what tags have been used (go to "`[website URL]/tags`" to see them all), and include any that are relevant to your post. Do not include the `#` symbol in the tags list. You don't need to do anything to "register" a new tag; just use it, and the tags list will be updated automatically.

After the second `+++`, write the content of your post, using any markdown formatting you like. See `content/posts/2015-02-02-Brett-BALSA-Interview.md` for a good example post.

### With Images/Attachments

To create a new blog post with images and/or attachments, create a new *subfolder* in the `content/posts` folder. Name the subfolder using the same file naming instructions described above (without the `.md` extension). Inside the subfolder, create a Markdown file named `index.md`, and use the template above to fill it with the necessary metadata and your content. Any image files (`.jpg` or `.png`) that you add to your new post subfolder will automatically be used to create an image gallery for the post. Any non-image files you add to your new post subfolder will be listed as attachments at the end of the post. See `content/posts/2018-10-02-Donut-Day` for a good example post.

## Specific Page Details

### Publications

The publications page is automatically generated from a CSV file, `content/publications/publications.csv`. Adding new rows to this table will automatically update the associated page (and the list of recent publications on the homepage).

### People

The people page is automatically generated from a CSV file, `content/people/people.csv`. Adding new rows to this table will automatically update the associated page. Any photos added to the `lab_photos` subdirectory will be added to the lab photo gallery at the bottom of the page. Photo filenames in the CSV file are specified relative to the `photos` subfolder.

### Journal Club

The journal club page is automatically generated from a CSV file, `content/journal_club/journal_club_papers.csv`. Adding new rows to this table will automatically update the associated page. To modify the page header, edit `content/journal_club/index.md`.

# Editing Styling, Templates, etc.

The site is built from a group of template specification files in the `templates` folder, and style sheets in the `sass` folder. To learn more about these, read the [Zola user guide](https://www.getzola.org/documentation/).

---

\* The distinction here is that `_index.md` represents a "section", which can contain subpages, whereas `index.md` indicates a single page.
