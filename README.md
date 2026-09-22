# LatticeLang - Conglang Toolset

LatticeLang is an in-progress tool for constructing natural-sounding languages. Unlike traditional generators, it incorporates **[Sonority Hierarchy](https://en.wikipedia.org/wiki/Sonority_hierarchy)**, and other '[linguistic universals](https://en.wikipedia.org/wiki/Linguistic_universal)' (more precisely, tendencies) and offers customization for experimental/alien languages if desired.

## Documentation
Documentation is available at [latticelang.readthedocs.io](latticelang.readthedocs.io).

- User Guide
- Theory
- Linguistics glossary
- Bibliography, notes, and research
- Archetecture
- Roadmap/Planning
- Decision archive
- API Reference: Technical details for developers including data contracts.

[![Docs Build](https://github.com/Danweel/LatticeLang/actions/workflows/docs-build.yml/badge.svg)](https://github.com/Danweel/LatticeLang/actions/workflows/docs-build.yml)

[![Read the Docs](https://readthedocs.org/projects/latticelang/badge/?version=latest)](https://latticelang.readthedocs.io/)

[![Deploy to Pages](https://github.com/Danweel/LatticeLang/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/Danweel/LatticeLang/actions/workflows/deploy-pages.yml)

## What does that mean?

Most phonology tools for conglangers focus on assigning IPA to CVC patterns. The classic example is Mark Rosenfelder (Zompist's) https://www.zompist.com/phono.html, https://www.zompist.com/gen.html. It's a site I've been to nearly since it's beginnings in the late 90's. It works, and for most conlangers it's plenty. I encourage the curious to play with those tools first and read the Language Construction Kit. You will get more out of the practice and discipline of constructing from scratch than a program can teach on its own.

That said, I wanted something that kept better track of the rules I was making, and helped me form a naturalistic language - of which there are many theories about the rules that underpin it. I'm not a linguist, nor are most conlangers, (though more than one has gone on to study in that field). This program borrows from some of the more popular observations about naturalistic languages to inform language creation. It's meant to be exploratory, not just slap guardrails on what should be an investigatory process. But I also wanted to make it a bit more approachable for novelists and game writers to play with these concepts.

## What it does, and why creators may find it useful.

Have you ever started naming towns and cities, and quickly find yourself running out of similar words that sound related? Have you started naming a cast only to get stuck at creating _even more names_ for their extended families that get mentioned once? I find this exhaustion comes from trying to keep the intuitive rules you created straight. Part of it is not being well versed enough in linuguistics to even know what those rules are - but people have enough of an innate sense to be able to sense when a language, even a 'naming language' is off.

'Faljut Uvaskafask' was a name from a naming language I created years ago using one of these generators and a lot of trial and error. That last name is U-vas-ka-fask - or is it U-vask-a-fask, maybe Uvask-afask? The distinction can matter when it comes to making up more words that fit the patterns.

Maybe you already have a list of words or names that you think seem to fit together already:

Cheusal
Joscioso
Palaiot
Raptan
Thilis
Dimiad
Venis
Spiro
Echor
Argyris
Spyris
Hrist
Stavros
Rinato
Rusil
Ryfon
Fanis
Lyko
Roda
Styl
Miro
Savas
Iaso
Silis
Myrto
Kapo
Yior
Lianol
Zino

Maybe they are cohearent, maybe not. It's hard for a layman to tell at a glance. But this is often where authors start, part of a manuscript that's starting to come together but now more names are needed - not just what might be recognizable as names but places too, which don't always sound like the proper nouns for people, and you start thinking about the language these people would have to speak to get names like that. There's something vaguely grecian or latin about these, but just copying rules from that similar language directly will lose the off-kilter direction these have.

When creating words without rules to start with there's no guarantee that these words even _do_ have the same rules. They may disagree with each other - though, throwing out the ones that don't fit isn't necessarily naturalistic either, which is an additional level of complexity you can return to later. You can probably already pick out a few that might buck the rules even without any knowlege at all - so can readers. But getting a baseline of more or less consistent words is easier said than done. You can pick at a tool like Gen until the words you get out reflect closely the list you already have. It takes a lot of time, and often, you're not learning very much, either - more than you knew before at least, but it's a lot of guessing unless you delve into the hobby at length.

I wanted a tool that let me put in a list of words (or 'corpus') and it could compute likely rules that seemed present. That's also easier said than done. I waited about twenty-five years for something to come across my attention that did this sort of thing and I never saw it. Linguists probably have some sort of tool that approximates this, but it's buried in papers, about a specific thing and likely too heavy-duty to use casually. Conlangers enjoy conlanging apart from writing - so do I. When I delve into it, it's to immerse myself in the ideas of it. Meanwhile, I write less, and other authors are still naming thier maps randomly, because getting that much into linguistics isn't a priority. But authors are curious, and if it was easier to get into, I'm sure they'd appreciate its insights for their worlds and worldbuilding. A "word generator" isn't really going to serve that community well.

## The problem

Analysis. Exactly how do you reverse engineer a corpus? Worse, a fairly tiny one? I suspect this is why no one's built this. I still have no solid reason to believe it'll work smoothly - probably not. But here's some assumptions I've made in the attempt:

### Theories

Linguistics is a science, and touches on a lot of fields. Acoustics, biology, neuroscience, anthropology, etc. It's a field of science _because_ we don't know exactly how it works. That means there's theories - competing theories. Which means, to build something like this you have to choose a few over others. Right now only the first module is mapped out when it comes to "constructing a language": Phonology - this will help us "generate words" - at least in the most basic sense. Here's some of the theories - i.e., assumptions, my program makes, some are more 'fundamental' than others. A full bibliography and glossary is in the docs, which I'm building as I go along and vet ideas.

#### Autosegmental Phonology

A word isn't just one 'linear' thing. Features are multiple things that work on simultaenious, 'parallel' tiers: melody (consonants and vowels), tone (pitch patterns), 'skeletal' (timing), etc - worse, each of these can 'spread' from one segement of a word to influence others, such as vowel 'harmony'. This goes beyond the basic phonotactics most generators deal with. This is only partially dealt with even in my archetecture, but I've left room for it.

#### Feature Geometry/Optimality Theory/Obligatory Countour Principle

Phonological features are not a flat list but can be organized in a tree hierarchically. Optimality theory proposes that constraints that are defined are not univesally strict and the one that is most optimal is the one that satisfies the hierarchy best. Finally, related to autosegmental phonology, two identical segments can't be ajacent to each other. "th" can't immediately follow "th" - in any language. These sound self-evident but they're actually rather large claims.

#### Sonority Scale/Sonority Sequencing Principle

This is the one I started with: In syllables, "sonority" - the resonance or sound-energy of a speech sound - rises from the start of the syllable (onset) to the middle (nucleus) and falls from the middle to the end (coda). Assumed to be more or less universal because of the physics involved, the sonority scale goes from "stops" to "vowels":

Stops < Affricates < Fricatives < Nasals < Liquids < Glides < Vowels

Examples of each:

Stops:      p, b, d, k, g
Affricates: ch, tch
Fricatives: f, v, s, sh
Nasals:     n, m
Liquids:    l, r
Glides:     y, w
Vowels:     a, i, o

From a layman's perspective, this seemed like an enormous help in getting the sound of a naturalistic language - it's easier to define exceptions when there's a trend to start with.

#### Accounting for adjacent vowels, haituses, diphthongs

Sometimes, two vowels appear next to each other but are not one sound - take Hawai'i, for example. That's a haiatus, and the analyser needs to be able to be instructed about them if they appear, meaning distinguishing between this and diphthongs are important - it's not just a matter of orthography, either - perhaps your writing system already handles that by spelling diphthongs with a single character vs multiple depending on the situation (something English does more poorly). You can still end up with times you'll have to guide your rules manually:

Example: "aibo-" In this example from Japanese we come across an immediate problem. The syllablery is a-i-bo-o. The common pronounciation though is closer to a diphthong though, and the final vowel is 'long'. Focussing on a nd i, the program needs to be flexible enough to handle a definition of a-i in terms of construction _and_ recognize the diphthong as existing. The long vowel is much easier to handle but also needs to be noted besides via orthography - how you intend to spell things.

### More challenges

These theories are not fully in alignment, OCP appears to be an absolute constraint, for example, where the program does not lock you in this way. "Serial generative derivation", which is the computation behind the genration (for now), does not really mesh well with autosegmental theory. Rough edges have to be glossed over - but the question is which and how much? This is a design question that doesn't have a correct answer. I suspect I'll have to do quite a bit of testing to evaluate if it's good enough. This is the advantage over scientifically rigorous tools, though. An element of art can enter into the picture. None of us should expect to generate a scientifically-naturalistic-language for real. That's not how languages develop. They are more organic than anything we can come up with, which is why we haven't figured out which rules truely are universal, which are tendancies and which are just 'common'. When coming up with fiction, those aspects are up to your own perception in large part, just like anything complex like drawing figures or writing about people. But I'd like it to be helpful.

### More traditional generation stuff included

#### Phonotactics

This is the CVC (consonant-vowel) patterns almost all word generators use. Some include weighting, and this one does as well, which means certain patterns are more likely than others.

#### Orthography & IPA

Speaking of how to spell things, authors need to be able to spell their language in a way readers can read it. While constructing the underlying rules will involve specifing specific sounds, which we use the International Phonetic Alphabet for, where ælbəm = album. Each character unambigulously represents a sound humans can make. While handy for defining things, it's mostly unreadable. ˈfɝðɚmɔɹ represents "furthermore". You'd have a lot more letters to memorize _just_ to deal with English. It's advisable, even if your language has a written component that doesn't resemble English, to use as many English/Latin/Roman characters as possible. Or whichever alphabet your readers are reading your book in. The program will help you with the rules for converting the phonology to its spelling in a regular way - that's nothing new, but it's built in.

#### Documenatation & Development

Documentation is being done from day one as the program develops. You can already view the entire plan for LatticeLang Phonology, including aspects left out for now. I have a documentation background, not a code background. The program has been deliberately designed in advance of any code.

I will then proceed to screw it all up with my best attempt at careful vibe-coding. This includes being cautious about security and dependancies. I plan to hand-guide and review everything I can. No pressing start and waiting three days for a result. This will be much closer to asking for specific algorhythms one at a time according to the established documentation. It's the only way I can verify if the program is even viable to begin with. It's possible that analysis with so few imputs is fully sillypants. To know its limitations and attempt to work with them, it has to be built one piece at a time.

This also means that if I/the AI fails in doing the code, someone else with a real coding background can pick up where I fell short, or a real linguist can intervene in the logic in a precise way. The idea is to make it as easy as possible for experts who notice a problem to make up for any holes. For me, this is a hobby, and a bit of a documentation project. It would also be interesting to see if human-organized documentation and guidance helps an agent build something less rickety - they're not reliable and I don't treat them as such.

I run as much AI on my local machine as possible, reducing reliance on large 'data-centers'. Where that wasn't possible, I've been using Proton's private AI, which is about 10$ a month for unlimited use, which is not a significant contribution to either the industry pockets nor handing over training data (for now). I do my best while managing this project to teach myself how a python project comes together and finally give this little program a shot. Hopefully I can rely less and less on vibing, especially if I can get others interested.
Once the project comes together a bit more, I have some lingustics and programmer friends that I can bother to look things over. For now I don't want to waste their time on a project that I might not finish.

Ultimately, I would love to create a full suite, something aimed at conglangers but with the strength of SIL's suite in terms of language and lexicon cappture - I was never 100% comfortable with the organization, despite it's significant contribution to language documentation and related tools/fonts/etc. It's a personal quibble - it's not exactly the right program for a conglang anyway.

#### Program stuff

- **Libre & Open**: Built with Python and customtkinter (common GUI), licensed under GPL-3.0. Fork to mess with the implementation or theories. Contribute upstream?
- **Project-based workflow**: Saving and managing more than one conlang. Working on different parts or modules at different times. Changes doesn't mean you have to start over from the initial steps.
- **Font options**: Comes packaged with v7 SIL fonts (Andika, Charis, Dolous, Gentium), Junicode 2, STIX 2, Liberation 2, Liguistics Pro (from the LinguaFranca>Heuristica>Utopia lineage), Open Sans (from the Noto>Droid Sans lineage), and GNU FreeFont to include a monospace character set, covering a wide variety of style options with near-total character coverage and encodings (Type 1, Open, TrueType, WOFF, etc.).

---

## License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.
See [LICENSE](LICENSE) for details.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

---

(Placeholder sections, a don't forget for me for later):

## Quick Start

### Ubuntu & Debian **Users**
```bash
pip install latticelang
latticelang
```

### Windows **Users**


### MacOS **Users**

---

## Setting up for Contributors
We welcome contributions!

### Types of Contributions
- Documentation: Improve tutorials, fix typos, add examples (no Python setup required)
- Code: Fix bugs, add features, improve performance, etc.
- Testing: Write unit tests, report bugs

### Guidelines
- CONTRIBUTING.md
- Docs links

### Quickstart for development (Setup Script)
#### For Linux Ubuntu and Debian:
1. Git clone or download the Github zip file
2. Run the bootstrap script to set up your environment:
```bash
./setupenvironment.sh
```

#### For Windows
?

#### For MacOS
?

### Manual Setup (Clone and Install)
**Recommended: Use Poetry for dependency management**
### Setting up for contribution
#### For Linux Ubuntu and Debian:
```
git clone https://github.com/danweel/latticelang.git
cd latticelang

poetry install --with dev
poetry run latticelang
```
#### For Windows
?

#### For MacOS
?

### Quick Start for contributing to the docs

#### For Linux Ubuntu and Debian:
1. Git clone or download the Github zip file
2. Run the bootstrap script to set up your environment:
```bash
./setupthedocs.sh
```

or manually:
```bash
poetry install --with docs
```

I recommend using [VSCodium](https://vscodium.com/) if you are new to contributing. If you do, use the following to obtain recommended extensions for the project:
(put here extensions quick link)

### Prerequisites (these will be checked for and installed by the bootstrap)
- Python 3.9+
- Poetry
- TBD
