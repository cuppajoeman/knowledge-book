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
<https://github.com/cuppajoeman/knowledge-book/blob/main/build/book.pdf>

## Structure of book {#structure-of-book .unnumbered}

The book is partitioned into different sections based on the domain it
is involved with. There may be shared definitions and theorems
throughout the chapters, but in general it will start more elementary
and get more advanced.

## Knowledge {#knowledge .unnumbered}

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

If you want to contribute to the project it's most likely that a
contribution will fall into one of the following categories

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

## Setup for Contributing {#setup-for-contributing .unnumbered}

In order to contribute to this project you will need to understand the
basics of git, LaTeXand the structure of the project works.

### Git {#git .unnumbered}

If you aren't familiar with what git is, I recommend you watch the
videos on the following page <https://git-scm.com/doc>, and remember the
link to the docs for future reference. To download the project you can
start by cloning the project onto your computer.

If you have access to a terminal then you can do the following:

::: term
git clone git\@github.com:cuppajoeman/knowledge-book.git
:::

From here on out you will make changes to the project and make commits
using git. Eventually you will want to upload online so that other users
can see your changes, in this case you will run

::: term
git push
:::

Otherwise you can download <https://desktop.github.com/>. And after
you've made edits to the book, you can push, then finally then go to
your forked version of the project and make a pull request into the main
project.

## Communication {#communication .unnumbered}

All communication will occur through github disccusions. You can access
it here:

## Content Based {#content-based .unnumbered}

If you want to add a new top level structure, the best thing to do is to
verify with other members of the project if it warrants it's own top
level structure, otherwise it can be added as a substructure of an
existing one.

Supposing that you are on linux, the easiest way to make a new structure
and start working on it:

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

### Creating Files {#creating-files .unnumbered}

For example if want to create a new definition for topology we would go
into the definition folder for topology and create a new file using
pothole case and don't include any extraneous words, for example it is
better not to append "the\" to the front of your file names when not
specifically required.

[^1]: But sometimes they escape, as their usage becomes more than just
    an intermediate step, as Zorn's or Fatou's Lemmas did

[^2]: <https://github.com/cuppajoeman/knowledge-book>

[^3]: <https://www.math.toronto.edu/cms/alfonso-memorial/>

[^4]: <https://math.univ-angers.fr/~campesato/>

[^5]: <https://www.galgr.com/>
