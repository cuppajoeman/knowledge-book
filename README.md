# Preface {#preface .unnumbered}

This book contains knowledge that that me or my peers have obtained, the
purpose is to explain things fundamentally and in full detail so that
someone who has never touched the subject may be able to understand it.
It will focus on conveying the ideas that are involved in synthesizing
the new knowledge with less of a focus on the results themselves.

It differs from a normal textbook in that it is open source and will
fall under more continuous development rather than having editions that
periodically come out. It also differs in the sense that it welcomes
other users to improve the book.

Here is a link to the book:
<https://raw.githubusercontent.com/cuppajoeman/knowledge-book/main/build/book.pdf>

## Structure of book {#structure-of-book .unnumbered}

The book is partitioned into different sections based on the domain it
is involved with. There may be shared definitions and theorems
throughout the chapters, but in general it will start more elementary
and get more advanced.

## Knowledge {#sec:knowledge .unnumbered}

In this book you will find many results, will will characterize them as
being one of the following

-   Theorems - Results that are of importantance and who's proof is not
    easily found (maybe using a novel idea)

-   Propositions - Results of less importance who's proof could be
    constructed without a novel idea

-   Lemmas - Results that are technical intermediate steps which has no
    standing as an independent result on first observation [^1]

-   Corollaries - Results which follow readily from an existing result
    of greater importance

## Recommendations {#recommendations .unnumbered}

By now you might know that in order to actually get better at
mathematics you have to engage with it. This book may be used as a
reference at times, but I highly recommend trying to re-prove statements
or coming up with your own ideas before instantly looking at the
solutions.

## About the companion website {#about-the-companion-website .unnumbered}

The website[^2] for this file contains:

-   A link to (freely downlodable) latest version of this document.

-   Link to download LaTeXsource for this document.

## Acknowledgements {#acknowledgements .unnumbered}

-   A special word of thanks to professors who wanted to make sure I
    understood and learned as much as possible Alfonso Gracia-Saz[^3],
    Jean-Baptiste Campesato[^4], Valentine Chiche-Lapierre and Gal
    Gross[^5]

-   Thanks to Z-Module, riv, PlanckWalk, franciman, qergle from #math on
    <https://libera.chat/>.

# Contributing {#contributing .unnumbered}

Contributions to the project are very welcome, let's delve into how to
get started with this.

Here is a list of things that can be worked on:

-   Content Based

    -   Adding Definitions, Theorems, ...

    -   Finishing TODO's

    -   Formatting of the book

-   Structural Layout of Project

    -   Organization

    -   Simplyfing the existing structure of the directories

    -   Making scripts which set up new structures

-   External

    -   Adding explanatory content to help onboard new users

    -   Getting others involved

    -   Creating infrastructure to support users (Github discussions)

## Example {#example .unnumbered}

I will describe how to do this in detail in the below paragraphs, here
is the TLDR of them. Let's say you have a theorem you'd like to add,
here is a quick outline of what you have to do. Fork the project, find
the structure that your theorem belongs in, one possible structure could
be first order logic, then go ahead and copy the blank `theorem.tex`
file to `my_new_theorem.tex`, after that write up your theorem, include
it in that structures content file, compile the project and verify it's
there, then push to your forked repository and create a pull request
against the main repository on github.

## Setup for Contributing {#setup-for-contributing .unnumbered}

In order to contribute to this project you will need to understand the
basics of git, LaTeXand the structure of the project.

### Git {#git .unnumbered}

If you aren't familiar with what git is, I recommend you watch the
videos on the following page <https://git-scm.com/doc>, and remember the
link to the docs for future reference.

Next you can make a github account on [github.com](github.com), the way
you will get a copy of the project is by forking the project. To do that
visit <https://github.com/cuppajoeman/knowledge-book> and click fork in
the top right corner, once you've forked it we can now download it to
our computer.

If you have access to a terminal then you can do the following:

::: term
git clone \<link gotten from your forked repo>
:::

From here on out you will make changes to the project and make commits
using git. Once you're happy with the changes you've made, you can save
your git commits online by running

::: term
git push
:::

Otherwise you can download <https://desktop.github.com/>. And after
you've made edits to the book, you can push, then finally then go to
your forked version of the project and make a pull request into the main
project. To do this visit your forked version of the project on github
and navigate to the pull requests tab, then make sure the base
repository is `cuppajoeman/knowledge-book` and add relevant info
explaining the pull request. Once someone has reviewed your changes it
will be merged into the main project.

### LaTeX {#latex .unnumbered}

This document is entirely written in LaTeXwhich is a language which lets
us format mathematics and make figures easily.

If this system is entirely new to you, then don't worry, you'll be able
to pick up most of what you need by looking at examples being used in
this project, otherwise take a look at
<http://www.docs.is.ed.ac.uk/skills/documents/3722/3722-2014.pdf>.

To be able to LaTeXup and running, it is dependent on the operating
system you are using, but the one thing that remains invariant is that
you will need a way to compile it and a way to edit it.

#### Compilers {#compilers .unnumbered}

1.  <https://miktex.org/> - windows

2.  <https://tug.org/mactex/> - mac

3.  <https://www.tug.org/texlive/> - linux

    -   Note this will probably be available in your distributions
        package repositories.

#### Editors {#editors .unnumbered}

1.  <https://tug.org/texworks/> - minimal

2.  <https://tug.org/texworks/>, <https://www.xm1math.net/texmaker/> -
    more fully featured

3.  vim, emacs, other terminal based editors

    -   Allows you to be the most efficient

Once you've obtained an editor, if it has some type of built-in compiler
then you will want to change the output directory to be the build
directory. This makes sure that when you compile the document that the
root directory of the project isn't filled with irrelevant files. For
each editor it will be different, but the general setup will be to get
to some sort of configuration panel (or file) and to change the editors
compile command to this: `pdflatex –output-directory=build`. Some
editors might have a built in mode for this, for example with tex maker
one can tick the "use build directory for output files\", for users who
use vim, there is a built in option for vimtex like so:

    let g:vimtex_compiler_latexmk = {
                \ 'build_dir' : 'build',
                \}

## Communication {#communication .unnumbered}

Feel free to ask any question on the discord server:
<https://discord.gg/ReceZrGuN6>, it will also be a place for general
discussion. Another option we can look at is github discussions.

## Content Based {#content-based .unnumbered}

To understand how to add content to the project, the best step is to
understand fundamentally what a structure is.

A **structure** is a directory which has the following :

-   content.tex

    -   This file includes all the content in the other directories of
        this directory

-   definitions

-   theorems

-   lemmas

-   lemmas

-   corollaries

-   sub_structures

    -   This directory contains other **structures**

Note that the other directories; definitions, theorems, lemmas, lemmas,
corollaries are non-recursive directories that contain content (Let's
call them content directories from now on) [see here](#sec:knowledge)
for exactly what these directories contain.

If you want to add a new structure, the best thing to do is to verify
with other members of the project if it warrants it's own structure,
otherwise it can be added as a substructure of an existing one.

Supposing that you are on a unix based operating system, then here is
how one could create a new structure:

### Manually {#manually .unnumbered}

::: term
cp -r structure new_structure cd new_structure mv content.tex
new_structure.tex nvim new_structure.tex
:::

Otherwise if you're adding a new theorem, it could be:

::: term
cd existing_structure/theorems cp theorem.tex my_new_theorem.tex nvim
my_new_theorem.tex \... git add -A && git commit -m \"add my new
theorem\" && git push
:::

### Using the Script {#using-the-script .unnumbered}

Alternatively for a more streamlined experience we can use some of the
scripts we have for creating new content. (Note that right now this
script is only for creating new content files, but eventually will
create new structures as well)

To get started make sure you have `fzf` installed and the python package
`pyperclip`.

First to learn about the script run:

::: term
python scripts/main.py -h
:::

And once you have read this we may create a new theorem like

::: term
python scripts/main.py t \"My new Theorem\" -c
:::

Which asks you for which structure the theorem should belong to and
creates the file for us, the -c option copies
$\texttt{\\input\{\textit{path to new theorem}/my\_new\_theorem\}}$ to
the clipboard so that it may be included in the main content file
associated with the structure.

### With gui {#with-gui .unnumbered}

If you're on windows or another operating system without access to
terminal, you can always take the directory `structure` and copy it to a
new name. To make new content file, go to the revelent content directory
and copy the blank bootsrap file, that is if you wanted to make a new
definition you can go to the structures definitions folder and then copy
`definition.tex` to `my_new_definition.tex` and start working on it.

[^1]: But sometimes they escape, as their usage becomes more than just
    an intermediate step, as Zorn's or Fatou's Lemmas did

[^2]: <https://github.com/cuppajoeman/knowledge-book>

[^3]: <https://www.math.toronto.edu/cms/alfonso-memorial/>

[^4]: <https://math.univ-angers.fr/~campesato/>

[^5]: <https://www.galgr.com/>
