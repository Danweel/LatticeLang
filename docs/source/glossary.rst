.. _glossary:

Glossary of Terms
=================

Creating here a glossary of terms, and determining which of sometimes several different names
we'll use for similar or identical concepts. Make note of competing theories or names. Try to be
consistent so we're not grabbing from everywhere at once in our naming scheme.

Each entry lists its terms one per line (stacked); every stacked
line registers as a linkable cross-reference target. Plural and
alternate names go on stacked term lines, not comma-separated.

New entries should maintain the cross-reference density shown here — terms should
reference related concepts, not stand alone.

Source Attribution
-------------------

   Definitions in this glossary draw on standard phonological
   description as presented in the International Phonetic
   Association's Handbook (1999), Chomsky & Halle (1968), and
   Clements (1990) for the sonority hierarchy. Entries marked
   ``LatticeLang-specific`` are project terms, not standard
   usage. Contested or non-obvious definitions cite their source
   inline; uncited entries reflect textbook consensus.

Glossary
========

.. glossary::
   :sorted:

   affricate
   affricates
      A single :term:`phoneme` consisting of a stop closure followed by
      frication release. Represented in :term:`IPA` with a tie bar (e.g.,
      /t͡s/, /t͡ʃ/). LatticeLang accepts non-tie-bar input (e.g., "ts")
      as an alias but normalizes to the tie-bar form internally. See
      :ref:`adr-028` and :ref:`dc_ipa_reference`.

   airstream mechanism
      How airflow is initiated to produce a sound. Lung air
      (pulmonic egressive) powers ordinary :term:`stops`,
      :term:`fricatives`, and vowels; glottalic pressure produces
      :term:`ejectives` (/tʼ/); glottalic suction produces
      implosives (/ɓ/); velaric suction produces clicks (as in
      Xhosa and Zulu). LatticeLang's MVP covers pulmonic sounds
      only; ejectives, implosives, and clicks are post-MVP input.

   allophone
   allophones
   allophonic
      A context-dependent variant of a :term:`phoneme`. e.g., in English,
      the phoneme /t/ has allophones [tʰ] (word-initial), [ɾ] (between
      vowels), and [ʔ] (word-final before another consonant). Allophonic
      rules are an advanced feature in LatticeLang. See
      :ref:`constraint-types-overview`, :term:`phoneme`.

   alveolar : place of articulation
      A manner of :term:`articulation` where the :term:`tongue tip` or
      :term:`blade` contacts the alveolar ridge, just behind the upper
      teeth. e.g., /t/, /d/, /n/, /s/, /z/.

   apical : anatomical
      Articulator, being the :term:`tongue tip`, as opposed to :term:`laminal`.
      The :term:`apical` vs :term:`laminal` distinction is :term:`phonemic`
      in some Australian languages and certain dialects of Basque.

   approximant
   approximants : manner of articulation
      A manner where articulators approach each other but do not create
      turbulent airflow. Includes :term:`liquids` (/l/, /r/) and
      :term:`glides` (/j/, /w/). Approximants are high on the :term:`sonority scale`.

   articulation
      The physical production of speech sounds, described by :term:`place` (where),
      :term:`manner` (how), and :term:`voicing` (vocal fold vibration).

   assimilation
      A phonological process where one :term:`segment` becomes more similar
      to an adjacent segment (e.g., /n/ → [m] before /b/). See :term:`harmony`.

   autosegmental phonology
      A theoretical framework (Goldsmith, 1976) in which some properties —
      notably tone and harmony features — exist on their own *tiers*,
      independent of individual consonants and vowels. A harmony feature
      "belongs" to a stretch of the word rather than to one segment, and
      spreads across it. Relevant to LatticeLang: the long-term design for
      ``cross_syllable_harmony`` and tone is autosegmental in spirit (see
      :ref:`q42-harmony-parameterization`'s upgrade paths); MVP models
      harmony as pairwise agreement instead, which is simpler and adequate
      for within-syllable scope.

   backness
   vowel backness
      Where the tongue's highest point sits on the front-back axis
      during a vowel — front /i/, central /ə/, back /u/. One of the
      three vowel descriptors with :term:`height` and :term:`rounding`.

   bilabial : place of articulation
      Both lips contact each other. e.g., /p/, /b/, /m/.

   bimoraic
     Containing exactly two moras. A common syllable type
     cross-linguistically; Japanese CVV and CVC syllables are
     typically analyzed as bimoraic. Contrast with
     :term:`monomoraic`.

   centering
      A :term:`diphthong` that glides toward a central vowel —
      historically schwa — as its second element. The classic
      set is non-rhotic English: /ɪə/ in "near", /eə/ in "square",
      /ʊə/ in "cure". Contrast :term:`falling` and :term:`rising`.

   click
   clicks : airstream mechanism
      A consonant produced with velaric ingressive airflow: the
      tongue seals against the velum while a second closure forms
      ahead of it; releasing the front closure pops air inward.
      Nearly exclusive to languages of southern Africa — Zulu,
      Xhosa, and the Khoisan family — but also found as paralinguistic
      sounds (the English "tsk-tsk"). Notated with a pipe or
      click letters: /ǀ/ (dental), /ǃ/ (alveolar), /ǁ/ (lateral),
      /ʘ/ (bilabial), /ǂ/ (palatal). Clicks may carry accompaniments
      (voicing, nasalization, ejective release), multiplying the
      inventory. Post-MVP input for LatticeLang, alongside
      :term:`implosive`.

   cluster
   clusters
      A sequence of two or more consonants within a single
      syllable constituent — an onset cluster (/spl/ in "splash")
      or coda cluster (/nts/ in "pants"). Governed by
      ``max_onset_length`` / ``max_coda_length`` caps, the
      sonority sequencing principle, and ``prohibited_clusters``.

   coda
   codas
      The consonant(s) at the end of a syllable, after the vowel nucleus.
      In the syllable /kæt/, /t/ is the coda. Coda length is constrained
      by :ref:`max_coda_length <constraint-types-overview>`.
      The final portion of a syllable, following the nucleus.
     In the MVP model, only consonants occupy coda slots;
      vowels in "closed" syllables are represented as
      tautosyllabic sequences (:term:`diphthong`) or as
      heterosyllabic :term:`hiatus`. :term:`moraic` analysis
      is post-MVP.

   complementary distribution
      When two sounds never occur in the same :term:`phonological environment`,
      they are likely :term:`allophones` of the same :term:`phoneme`. Contrast
      with :term:`minimal pair`.

   complex nuclei
      Nuclei containing more than one vocalic element. Two
      distinct instantiations: (1) :term:`diphthong` — one
      phoneme filling one nucleus slot; (2) :term:`heterosyllabic`
      sequences where two nuclei sit adjacently (hiatus) or a
      vowel occupies a non-nuclear slot. The distinction is
      structural: diphthongs move as units through constraints
      and merges (:ref:`ADR-040`), vowel sequences don't.

   consonant
   consonants
      A speech sound produced with a constriction in the vocal tract
      that impedes airflow. Characterized by :term:`place`,
      :term:`manner`, and :term:`voicing`.

   constraint
   constraints
      A rule that filters candidate syllables during generation. A
      candidate either passes or fails the constraint (in the current
      Generative/Rule-Based mode). See :term:`constraints` for the
      complete catalog. See :ref:`uc03` for user-facing definition.

   CoNLL-U
      A plain-text, tab-separated file format for encoding annotated
      linguistic data, primarily used by universal dependencies.
      Not directly relevant to LatticeLang's initial phonology focus, but noted as
      a design philosophy for data interchange (simplicity, extensibility
      via a "misc" field). See :ref:`q21-conllu-interchange`.

   coronal : place of articulation
      Sounds articulated with the :term:`tongue tip` or :term:`tongue blade`
      (:term:`dental`, :term:`alveolar`, :term:`postalveolar`, :term:`retroflex`).
      A :term:`natural class` in :term:`feature geometry`.

   dental : place of articulation
      The tongue tip contacts the upper teeth. e.g., /θ/, /ð/.

   diphthong
   diphthongs
      A vowel sequence functioning as a single syllabic unit, where the
      tongue moves from one position to another (e.g., /aɪ/ in "eye").
      Classified as :term:`falling`, :term:`rising`, or :term:`centering`.
      Diphthongs (e.g., /aɪ/, /oʊ/) are single phonemes of category
      ``diphthong`` occupying the nucleus slot. Input accepts the bare
      sequence (``"aɪ"``); the non-syllabic diacritic (aɪ̯) is accepted
      but normalized to the bare form. No tie bar is used — the tie bar
      exclusively marks consonant-affricate unity (ADR-028). Unlike
      affricates, diphthong components are individually meaningful:
      the component vowels /a/ and /ɪ/ should exist in the inventory,
      and the system warns if they don't. Custom symbols not present
      in the IPA reference table are accepted but flagged, and receive
      no automatic features, rarity tier, or frequency data until reviewed.
      See :ref:`dc_ipa_reference` for the diphthong reference.
      Tautosyllabic by definition (one phoneme can't span syllables).
      In LatticeLang: one segment with ``components`` field,
      ``syllabic: "+"``, and a single slot occupation. Contrast with
      :term:`hiatus` (adjacent syllables) and :term:`complex nuclei`
      (general term covering both).


   dorsal : place of articulation
      Sounds articulated with the tongue body (:term:`velar`,
      :term:`uvular`). A :term:`natural class` in :term:`feature geometry`.

   duration
      Temporal length of segments or syllables. Correlates with
      :term:`mora` count (bimoraic > monomoraic). Phonetically
      measurable; phonologically encoded via moraic or geminate structures.

   epenthesis
      Insertion of a :term:`segment` not present in the underlying form.
      Related to :term:`faithfulness constraints` (DEP-IO, post-MVP). e.g.,
      Inserting a schwa to break up an impossible :term:`cluster`.

   ejective
   ejectives : airstream mechanism
      A consonant produced with a glottalic egressive airstream
      mechanism: the glottis closes, trapping air, then the oral
      closure releases. Notated with a trailing apostrophe
      (e.g., /tʼ/). :term:`ejectives`, :term:`implosives`, :term:`clicks`.
      Rare cross-linguistically. See :ref:`dc_ipa_reference`.

   faithfulness constraint
   faithfulness constraints
      A constraint from :term:`optimality theory` that penalizes deviation
      from the underlying input form. Types include MAX-IO (no deletion)
      and DEP-IO (no insertion). See :ref:`theoretical_framework`.

   falling
      A :term:`diphthong` whose first component is more prominent —
      closer to the syllable peak — with the second element gliding
      away from it. English diphthongs are typically falling:
      /aɪ/ in "eye" (/a/ peaks, /ɪ/ off-glides), /oʊ/ in "go".
      Contrast :term:`rising` and :term:`centering`.

   feature
   features
      A phonological attribute of a sound (e.g., [+voice], [+nasal], [+labial]).
      Features define :term:`natural classes` and enable constraints
      like :term:`OCP` and :term:`harmony`. See :term:`feature geometry`.

   feature geometry
      A phonological theory where features are hierarchically organized
      in trees. :term:`natural classes` emerge from shared subtree structure.
      Explains assimilation patterns precisely. LatticeLang uses features for
      :term:`OCP` constraint matching without full geometric hierarchy. See
      :ref:`theoretical_framework`.

   fricative
   fricatives : manner of articulation
      Continuous turbulent airflow through a narrow constriction. e.g., /f/, /v/, /s/, /z/, /θ/, /ʃ/.

   generative phonology
   SPE
   Sound Pattern of English
      A phonological theory using ordered, derivational rules to transform
      :term:`underlying forms` into the :term:`surface forms`. LatticeLang's
      primary theoretical framework the MVP aims at for proof of concept.
      ":term:`SPE`" refers to Chomsky & Halle's *The Sound Pattern of English* (1968).
      See :ref:`theoretical_framework`. See :term:`The Sound Pattern of English`.

   geminate
   gemination
      A doubled or lengthened consonant (e.g., Italian /tt/ in "mamma").
      The :ref:`no_geminate_obstruents <constraint-types-overview>`
      constraint prohibits identical adjacent :term:`obstruents`.
      A doubled consonant that spans two moras or syllable
      boundaries. In LatticeLang's MVP, geminates are modeled
      as two separate segment positions across a syllable
      boundary (e.g., onset of syllable N+1 repeats coda of
      syllable N). Full geminate constraint families are post-MVP.

   geminate halves
      The two moracic portions of a geminate consonant. In
      mora-based analyses they're treated as a single phonological
      unit; in the MVP slot model they appear as separate
      instances in adjacent syllables.

   glide
   glides
   semivowel
   semivowels
      A vowel-like sound functioning as a consonant - /j/ (as in "yes") and
      /w/ (as in "wet"). Phonetically, glides are essentially short vowels
      ([i] → [j], [u] → [w]); phonologically they behave as onsets — they
      cannot be syllable nuclei. This dual nature is why LatticeLang gives
      glides their own category (ADR-032). They are −syllabic and −consonantal,
      fitting neither the consonant nor vowel bucket cleanly.

   glottal : place of articulation
      Constriction at the glottis (vocal
      folds). e.g., /h/ (voiceless) and the glottal stop /ʔ/.

   harmony
      A requirement, enforced as a constraint, that features agree
      across :term:`segments`, e.g., :term:`vowel harmony` in Turkish,
      nasal harmony. In LatticeLang MVP, harmony operates within
      a single syllable only; cross-syllable harmony is deferred
      to post-MVP. See :ref:`constraint-types-overview` and
      :ref:`q23-universal-override-model`.

   height
   vowel height
      How open the jaw is during a vowel — the vertical dimension
      of vowel quality: close (/i u/), close-mid (/e o/), open-mid
      (/ɛ ɔ/), and open (/a/). One of the three vowel descriptors
      with :term:`backness` and :term:`rounding`.

   heterosyllabic
      Belonging to different syllables. Applied to vowel
      sequences (/a.i/ = two syllables), contrast with
      :term:`tautosyllabic`. Also applies to segments in
      different syllables vs. within one syllable.

   hiatus
      Two vowel sounds in adjacent syllabic positions, belonging to
      *different syllables* (e.g., "re.act"). Contrast with a
      :term:`diphthong`, where two vowel qualities form a single
      phoneme in a single nucleus, and with a glide + vowel sequence
      (e.g., /ja/), where the glide sits in a margin slot. All three
      structures express "two vowel-like letters in a row" and are
      distinct in LatticeLang: diphthong = one phoneme (:ref:`ADR-028`),
      hiatus = adjacent syllables, glide sequence = margin + nucleus
      (:ref:`ADR-034`).

   homorganic
      Sharing the same place of articulation, e.g., /n/ and /t/
      are homorganic (both are :term:`alveolar`). Relevant to
      :term:`assimilation` and :term:`OCP`.

   implosive
   implosives : airstream mechanism
      A consonant produced with glottalic ingressive airflow:
      the glottis closes and moves *downward*, rarefying air in
      the oral cavity so it flows inward on release. Roughly a
      quarter of the world's languages have them, especially in
      Africa and Southeast Asia, and they are nearly always
      voiced. Notated with a hook-top letter: /ɓ/, /ɗ/, /ʄ/,
      /ɠ/, /ʛ/. Often used as the "hard" counterpart to plain
      voiced stops, e.g., Hausa /ɓ/ vs. /b/. Post-MVP input for
      LatticeLang — ejectives, implosives, and clicks share the
      non-pulmonic exclusion.

   intonation
      Pitch variation over whole phrases and sentences, used for
      pragmatic meaning (question rise vs. statement fall,
      sarcasm, emphasis) rather than to distinguish words.
      Contrast with tone, which distinguishes words within the
      lexicon. Sentence-level and discourse-level by nature —
      outside LatticeLang's scope, which bottoms out at the word.

   IPA
   International Phonetic Alphabet
      A standardized system for representing the sounds of spoken
      language. Each symbol corresponds to exactly one :term:`phone`. See
      :ref:`dc_ipa_reference` and :cite:p:`ipa1999`.

   labial : place of articulation
      Sounds articulated with the lips, :term:`place of articulation`. A
      :term:`natural class` in :term:`feature geometry`. See
      :term:`bilabial`, :term:`labiodental`.

   labiodental : place of articulation
      Lower lip contacts upper teeth. e.g., /f/, /v/.

   labialization
   labialisation : secondary articulation
      A :term:`secondary articulation` where the lips round while
      the tongue performs a different primary constriction.
      Mark - ʷ, e.g., /kʷ/ — /k/ with simultaneous lip rounding.
      Common where vowels lost rounding historically (Latin /kʷ/
      surviving as Spanish /k/ before rounded vowels, English
      "queen" /kwiːn/ as [kʷ]-colored).

   laminal
   tongue blade
   blade : anatomical
      Contact descriptor contrasting with apical within coronals. Articulated
      with the tongue blade (just behind the tip), as opposed to :term:`apical`.
      Contrast: :term:`laminal` vs :term:`apical` distinguishes some sounds
      in Australian languages.

   lateral
   laterals
   lateral approximant
   lateral approximants : manner of articulation
      Airflow directed around the side of the tongue. e.g., /l/.

   larynx : anatomical
      The cartilage-encased structure in the throat housing the
      :term:`vocal folds`. Adjusting the vocal folds changes
      airflow through it and produces voicing contrasts. Known
      colloquially as the voice box or Adam's apple.

   lenition
   spirantization
   spirantisation
   weakening
      A class of sound changes in which a consonant becomes "weaker"
      or "softer" — easier to articulate. Common lenition pathways:
      Voicing (/t/ → /d/), Spirantization (a stop becoming a fricative,
      /t/ → /θ/), Debuccalization (losing oral place, /s/ → /h/), Vocalization
      (becoming a glide or vowel, /l/ → /w/), **Spirantization** is
      specifically the change of a stop into a fricative (/p/ → /f/,
      /k/ → /x/) and is one of the most common lenition processes
      cross-linguistically. Relevant to LatticeLang in sound change
      module. Similar to :term:`lenition` where a :term:`stop` becomes
      a :term:`fricative`. Related to :term:`markedness`.


   light syllable
      A :term:`syllable` weighing one :term:`mora`: a single short
      vowel in the :term:`nucleus` with no :term:`coda`. Contrast
      with heavy syllables (long vowel, diphthong, or closed
      syllable) at two. The weight distinction drives
      quantity-sensitive :term:`stress` systems — post-MVP in
      LatticeLang.

   liquid
   liquids
      A cover term for :term:`lateral approximants` (/l/) and
      :term:`rhotics` (/r/). Liquids are :term:`sonorants`,
      high on the :term:`sonority scale`.

   manner of articulation
   manner
      How a speech sound is produced in terms of airflow
      constriction: :term:`stop` (plosive), :term:`fricative`, :term:`affricate`,
      :term:`nasal`, :term:`approximant`, :term:`lateral`, :term:`trill`,
      :term:`tap`, :term:`sibilant` (subtype).

   markedness
   marked structure
   marked structures
      A concept central to :term:`optimality theory`, referring to how unusual
      or disfavored a structure is cross-linguistically. :term:`marked structures`
      are rarer, harder to learn, and tend to be avoided. :term:`markedness constraints`
      penalize them.

   markedness constraint
   markedness constraints
      A constraint that penalizes structurally disfavored outputs
      regardless of the input. Contrast with :term:`faithfulness constraint`.
      In Generative Phonology mode, markedness constraints function
      as hard filters.

   minimal pair
   minimal pairs
      Two words differing in exactly one phoneme, proving that those
      sounds are distinct phonemes (e.g., English "pat" vs "bat" proves
      /p/ ≠ /b/). Contrast with :term:`complementary distribution`.
      Used to establish phonemic contrast. Imported corpora lacking
      minimal pairs may indicate under-specification in the inferred inventory.

   monomoraic
      A syllable consisting of a single mora (weight unit). Typically,
      a short vowel or a coda-less syllable.

   mora
   morae
   moraic
      A unit of :term:`syllable weight`. Light syllables have one mora, heavy
      syllables have two. Relevant for :term:`stress` and :term:`tone` assignment
      (post-MVP). See :ref:`constraint-types-overview`.
      A unit of phonological timing that may or may not align
      with a syllable. In Japanese, each vowel contributes one
      mora, so /ai/ is two moras even when in a single syllable.
      Moras drive poetic meter (haiku) and syllable weight
      calculations. :ref:`dc_syllable_template` MVP uses
      onset/nucleus/coda slots; per-mora structures are
      post-MVP (validation rule 1). See also: :term:`bimoraic`.

   moraic consonant / moraic obstruent
      A consonant that occupies its own moracic slot rather
      than attaching to a preceding vowel. In Japanese, the
      moraic nasal /N/ and the first half of geminates are
      moraic obstruents. The term emphasizes the consonant's
      contribution to syllable weight, not its margin position.

   moraic slot
      A timing unit that may hold a vowel, consonant, or nasal.
      Post-MVP feature; MVP uses traditional onset/nucleus/coda
      trichotomy. Japanese's vowel-in-coda phenomenon (see
      below) is most naturally described using moraic slots
      rather than marginal codas.

   morpheme boundaries
      The edges between meaning-bearing units. Morpheme
      boundaries can block phonological processes (e.g.,
      Japanese compound boundaries preserve moraic integrity).
      LatticeLang's current model treats words as opaque
      strings; morpheme-level constraints are post-MVP.

   movement as unit
      A diagnostic for phonological constituency. If two
      elements pattern together in all phonological processes
      (metathesis, truncation, tone spreading), they form a
      single phonological unit. Diphthongs exhibit this
      behavior; hiatus sequences don't.

   nasal
   nasals : manner of articulation
      Airflow through the nasal cavity with oral closure. Mark ~,
      e.g., /m/, /n/, /ŋ/. Also a :term:`feature`, [+nasal].

   natural class
   classes
   natural classes
      A group of speech sounds that share one or more distinctive
      :term:`features` and behave alike in the :term:`phonology` of a language.
      Natural classes are the basic unit of phonological generalization:
      phonological rules and constraints almost always target classes,
      not individual sounds. e.g., **Obstruents** — stops,
      fricatives, and affricates, **Sonorants** — nasals, liquids, and glides,
      **Labials** — /p, b, f, v, m, w/ (all articulated with the lips),
      **Coronals** — /t, d, s, z, n, l, ʃ, θ/ (articulated with the
      tongue tip or blade at the alveolar ridge or forward). Natural
      classes form a *hierarchy*: all stops are obstruents,
      all obstruents are consonants. Which grouping is relevant
      depends on the phenomenon. e.g., if /p, t, k/ pattern
      together in some rule (say, aspiration), the relevant natural
      class is "voiceless stops" — the features they share. The test
      for whether a class is *natural* (rather than just arbitrary):
      languages treat the shared features as significant. If a
      language fronts all its back vowels before palatals, the
      class "back vowels" is behaving as a natural class. LatticeLang
      uses natural classes implicitly in two constraint types:
      ``ocp`` (blocks adjacent segments sharing a feature, which
      defines a natural class) and ``harmony`` (requires feature
      agreement across segments). The planned Feature Geometry model
      (see :ref:`theoretical_framework`) organizes natural classes
      into a hierarchy tree. See also: :term:`sonority`,
      :term:`feature geometry`. Defined via :term:`feature geometry`.

   nucleus
   nuclei
      The central, most :term:`sonorous` element of a :term:`syllable`,
      typically a vowel or diphthong. In the syllable /kæt/, /æ/ is
      the :term:`nucleus`.

   obligatory contour principle
   OCP
      A constraint preventing adjacent segments from sharing the same
      phonological feature (e.g., two labial consonants in a row, or
      two high tones). Originates from :term:`autosegmental phonology`,
      adopted by :term:`OT`. See :ref:`constraint-types-overview` and
      :ref:`theoretical_framework`.

   obstruent
   obstruents : natural class
      A :term:`natural class`. Sounds with significant airflow obstruction;
      :term:`stops` and :term:`fricatives`. Contrast with :term:`sonorant`.

   onset
   onsets
      The :term:`consonant`/s at the beginning of a :term:`syllable`,
      before the :term:`nucleus` (typically a vowel). In the syllable
      /kæt/, /k/ is the onset. Onset length is constrained by
      :ref:`max_onset_length <constraint-types-overview>`.

   optimality theory
   OT
      A phonological theory where constraints are violable and ranked;
      the optimal candidate is the one that best satisfies the hierarchy.
      See :ref:`theoretical_framework`.

   palatal : place of articulation
      A :term:`place of articulation`, tongue body contacts the hard
      palate. e.g., /j/.

   palatalisation
   palatalization : secondary articulation
      A phonological :term:`secondary articulation`, mark - ʲ,
      e.g.: /tʲ/  It can also mean a :term:`process` related to historical or
      abstract phonology. e.g., /t/ → /tʲ/ before front vowels. See :term:`assimilation`.

   pharynx : anatomical
      The muscular tube connecting the mouth and larynx to the
      esophagus and nasal cavity — the throat. Constrictions here
      produce :term:`pharyngeal` sounds (/ħ/, /ʕ/) and :term:`pharyngealization`;
      the :term:`tongue root` is its front wall.

   pharyngeal : place of articulation
      A constriction in the :term:`pharynx` (throat).

   pharyngealisation
   pharyngealization : secondary articulation
      A :term:`secondary articulation` where the :term:`tongue root`
      constricts the :term:`pharynx` during another articulation.
      Mark - ˤ, e.g., Arabic "emphatic" /sˤ/.

   PHOIBLE
      A cross-linguistic phoneme inventory database containing 3,020
      inventories across 2,186 languages. Licensed CC-BY 4.0. LatticeLang's
      primary IPA reference data source. See :ref:`bibliography`
      and :cite:p:`moran2019`.

   phone
   phones
      A physically observable speech sound, regardless of its phonological
      status. Phones are written in brackets: [tʰ]. Contrast with
      :term:`phoneme`. Written in slashes, /t/. See :term:`segment`.

   phoneme
   phonemes
   phonemic
      The smallest contrastive unit of sound in a language. Abstract
      mental representation that may have multiple :term:`allophone`.
      Written between slashes, /t/. See :ref:`UC-01_define_phoneme_inventory`,
      :term:`segment`.

   phoneme category
      The four-way classification of a phoneme as consonant,
      vowel, glide, or diphthong, derived from its features
      (ADR-032). Glides get their own category because they fit
      neither the consonant nor the vowel bucket cleanly.
      :ref:`uc01` step 2 proposes the category; the user
      confirms or overrides.

   phoneme inventory
      The complete set of :term:`phonemes` in a language. The starting point for
      LatticeLang — users define which sounds exist before specifying
      how they combine. See :ref:`UC-01_define_phoneme_inventory`.

   phonetic vs phonological
      Distinction between physical acoustic properties
      (phonetic) and abstract, contrastive categories
      (phonological). The segmenter bridges this gap by
      mapping acoustic-adjacent input to phonological categories
      (:ref:`UC012`). A diphthong may be phonetically similar
      to a vowel sequence while being phonologically distinct.

   phonological environment : LatticeLang-specific
      The surrounding material that a rule refers to — the
      segments before or after the one being affected. In a rule
      "a → b / X __ Y", "X __ Y" is the environment (X precedes,
      Y follows). Environments are what distinguish contextual
      romanization rules (post-MVP for LatticeLang) from plain
      segment mappings, and what the reverse pipeline must
      reconstruct when parsing romanized text back to IPA.

   phonological process
   phonological processes
      Systematic changes affecting sequences of phonemes
      (assimilation, deletion, epenthesis, etc.). The
      constraint-based validation in :ref:`dc_constraints`
      captures some process effects (OCP, harmony), but full
      generative rules are post-MVP.
      Singular form emphasizes individual rules (e.g., "nasal place
      assimilation" is one process).

   phonological rule : LatticeLang-specific
      An ordered transformation mapping an underlying form to a
      surface form ("make /t/ voiced between vowels"). Natural
      languages run many, ordered; linguists notate them
      "a → b / environment". LatticeLang treats rules as
      generation-side filters in the MVP — constraints reject
      candidates rather than rewriting them — with
      ``allophonic_rules`` (reserved, post-MVP) as the eventual
      home of genuine rewrite rules.

   phonological unit
      A generic term for any segment, syllable, mora, or
      prosodic category that participates in phonological
      patterns. The :term:`movement as unit` test establishes
      whether a sequence qualifies as a single unit.


   phonology
      The sound system of a language — its inventory of
      :term:`phonemes`, their combinations, and their alternations;
      by extension, the study of sound systems. The word LatticeLang
      docs reach for when distinguishing "the system" from "the
      sounds".

   phonotactics
      The rules governing which sound combinations are permissible in a
      language — which :term:`onsets`, :term:`codas`, and :term:`clusters`
      are allowed. See :term:`OCP`, :ref:`UC-03_define_phonotactic_constraints`.

   place
      Where :term:`articulation` takes place. See :term:`bilabial`,
      :term:`coronal`, :term:`dental`, :term:`dorsal`.

   place of articulation : place of articulation
      Where in the vocal tract a consonant's constriction occurs. :term:`bilabial`,
      :term:`labiodental`, :term:`dental`, :term:`alveolar`, :term:`postalveolar`,
      :term:`pharyngeal`, :term:`palatal`, :term:`velar`, :term:`uvular`,
      :term:`glottal`, :term:`retroflex`.

   postalveolar : place of articulation
      A :term:`place of articulation`, tongue blade contacts the area just behind
      the alveolar ridge. e.g., /ʃ/, /ʒ/, /tʃ/, /dʒ/. Alveolo-palatal is closely
      related to this group.

   process
   historical process
      A rule or sound change that maps one segment to another over time — input,
      output, environment. Assimilation, lenition, epenthesis, harmony, :term:`velarization` are all
      processes. They live in the abstract phonology (or in historical phonology).

   prosody
      Suprasegmental aspects of speech: :term:`stress`, :term:`tone`,
      :term:`intonation`, :term:`rhythm`. Operates above the level of individual
      :term:`segments`. Post-MVP in LatticeLang. See :ref:`constraint-types-overview`.

   retroflex : place of articulation
      Tongue tip curled upward and back toward the hard palate. e.g., Hindi /ʈ/, /ɖ/;
      Swedish (in some dialects) /ɳ/. One of the :term:`coronal` places.

   rhotic
   rhotics
      A cover term for "r-like" sounds: taps, trills, and approximant /r/. High
      :term:`sonority`, language-specific in behavior.

   rhythm
      The timing "feel" of speech — where stressed syllables
      fall relative to others. Classified impressionistically as
      stress-timed (English), syllable-timed (Spanish), or
      mora-timed (Japanese), though modern phonetics treats the
      distinction as gradient rather than categorical. Emerges
      from stress placement; hence post-MVP together with it.

   rising
      A :term:`diphthong` whose second component is more prominent
      (closer to the syllable peak), e.g., Spanish /je/ in *tierra*
      or /ai̯/ in *aire* in careful speech. Rare in English.
      Contrast :term:`falling`.

   rounding
   rounded
      A vowel feature: lips form a circular shape. Contrasts with
      :term:`unrounded`. Affects :term:`harmony` in some languages
      (e.g., Turkish). One of the three vowel descriptors
      with :term:`backness` and :term:`height`.

   secondary articulation : secondary articulation
      A simultaneous fact about how a single segment is produced:
      a lesser constriction layered on top of the primary one,
      coloring the segment without displacing its
      :term:`place of articulation` or :term:`manner of articulation`.
      The full set is labialization (/kʷ/), palatalization (/tʲ/),
      velarization (English "dark l" /ɫ/), and pharyngealization
      (Arabic emphatics /sˤ/); nasalization (/ã/) is sometimes added
      to the list. Marked with IPA diacritics. Contrast with a
      :term:`phonological rule`, which transforms a segment over
      time rather than modifying its production.

   segment
   segments
      An individual speech sound in a linear sequence, :term:`phonemes` and :term:`phones`
      are both :term:`segments`. The basic unit that LatticeLang manipulates.

   sibilant
   sibilants : natural class
      A subtype of fricative/affricate with high-frequency
      turbulence. e.g., /s/, /z/, /ʃ/, /ʒ/, /t͡s/, /t͡ʃ/, /d͡ʒ/.

   sejunct
      A term sometimes used for heterosyllabic vowel sequences,
      especially in Japanese phonology literature. Less common
      than "hiatus"; see that entry.

   sonorant
   sonorants : natural class
      Sounds with spontaneous voicing and relatively open
      vocal tract. Includes :term:`vowels`, :term:`nasals`, :term:`liquids`, :term:`glides`.
      Contrast with :term:`obstruent`. See :term:`sonority`.

   sonority
   sonority scale
   sonorous
      The acoustic openness/resonance of a speech sound —
      roughly, how much sound energy it carries. Stops carry
      least; vowels carry most. Languages arrange sounds on a
      sonority scale (least to most sonorous):
      Stops < Affricates < Fricatives < Nasals <Liquids < Glides < Vowels.
      LatticeLang encodes this as ``sonority_rank`` (0–9) on
      each phoneme (uc01, step 4), and uses ranks to enforce the
      :term:`sonority sequencing principle` and to plausibility-check
      ranks against a phoneme's features. See :ref:`theoretical_framework`
      for theoretical background.

   sonority sequencing principle
   SSP
      The near-universal constraint on syllable structure: within
      a :term:`syllable`, :term:`sonority` rises from the
      onset toward the nucleus and falls from the nucleus toward
      the coda, peaking at the nucleus — a "sonority peak" at
      the syllable's heart. See also :cite:p:`clements1990`. In
      "strength" /strɛŋθ/ - **Onset**: /s/ (fricative) → /t/ (stop) →
      /ɹ/ (liquid) — the /s/→/t/ fall *violates* the SSP;
      /s/-clusters are the classic exception (see the
      ``allow_s_appendix`` constraint). **Nucleus**: /ɛ/ (vowel) —
      peak. **Coda**: /ŋ/ (nasal) → /θ/ (fricative) — sonority falls.
      Implemented in LatticeLang as the ``sonority_sequencing``
      constraint type (see :term:`constraints`), with ``allow_s_appendix``
      as the explicit /s/+C exception.

   The Sound Pattern of English
      The 1968 book by Chomsky & Halle (often abbreviated **SPE**)
      that founded :term:`generative phonology`. Its formalism —
      ordered rewrite rules operating on feature matrices — is the
      direct ancestor of LatticeLang's constraint engine. Cited as
      :cite:p:`chomsky1968`.

   stop
   stops
   plosive
   plosives : manner of articulation
      Complete closure of the vocal tract, released as a burst. e.g., /p/, /b/, /t/, /d/, /k/, /ɡ/.

   stress
      The relative prominence of a syllable within a word —
      what English speakers hear as the capitalized part of
      "um-BREL-la". Realized through pitch, duration, and
      amplitude; because no single acoustic cue defines it,
      stress is a metrical abstraction. Patterns include fixed
      stress (always the initial syllable, e.g., Czech) and
      weight-sensitive stress (Latin, English). ``stress_assignment``
      and ``foot_structure`` are reserved post-MVP constraint
      types pending metrical machinery. Related: rhythm.

   stress assignment
      The process of designating syllables as stressed/unstressed
      within a word. Separate from tone (autosegmental feature)
      and quantity (moraic count). Post-MVP in LatticeLang; MVP
      assumes no lexical stress or handles it via simple
      positional rules.

   suprasegmental
      An umbrella term for properties that extend over more than
      one segment: stress, tone, intonation, and prosodic rhythm —
      "above the segments" (Latin: supra). Contrast with
      segmental features like voicing or nasality, which belong
      to a single phoneme. Suprasegmentals are post-MVP in
      LatticeLang (tone being a possible early exception), but
      the segmental/suprasegmental divide drives real design
      decisions: stress and foot structure need metrical
      machinery, tone needs tone-bearing units (TBUs).

   surface form
   surface forms
      The actual pronounced form, after all phonological rules have
      applied. In :term:`generative phonology`, derived from the
      :term:`underlying form`.  In LatticeLang, the output of the
      generator after constraint filtering.

   syllable
   syllables
      A unit of organization for speech sounds, consisting of an :term:`onset`,
      :term:`nucleus`, and :term:`coda`. The primary unit LatticeLang generates and
      validates. See :term:`syllable template`.

   syllable template
   CV skeleton
   prosodic template
      A structural pattern describing permitted syllable shapes,
      using C for consonant and V for vowel. The formal notation
      used in LatticeLang for defining permitted syllable
      structures. e.g., CV, CVC, CCV, CVCVV.  prosodic template
      is more common in prosodic morphology.See
      :ref:`UC-02_define_syllable_templates`, :term:`syllable`.

   syllable weight
   moraic weight
      Whether a :term:`syllable` is light (one :term:`mora`) or
      heavy (two :term:`morae`). Determined by nucleus length
      and :term:`coda` presence. Relevant for stress and tone
      assignment (post-MVP). See :term:`mora`.

   tap
   flap : manner of articulation
      Brief contact between articulators. Sometimes
      distinguished from "flap", based on tongue motion direction. e.g., the
      American English /ɾ/ in "butter."

   tautosyllabic
      Belonging to the same syllable. The decisive criterion
      separating a :term:`diphthong` (/aɪ̯/ — one phoneme, one nucleus
      slot, moves as a unit through constraints and merges,
      ADR-040) from a vowel sequence or glide onset (two phonemes,
      two structural positions). A diphthong is *tautosyllabic by
      definition* — a "diphthong" that crossed a syllable boundary
      would simply be hiatus. Diagnostic tests: can the sequence be
      split by morpheme boundaries or a pause? Do the elements count
      separately for meter? Does the language treat the pair as a
      unit in phonological processes? Japanese /ai/ answers these
      differently than English /aɪ/ — see the diphthong entry's
      contrast note. Applied to vowel
      sequences (/a.i/ = two syllables), contrast with
      :term:`tautosyllabic`. Also applies to segments in
      different syllables vs. within one syllable.

   tie bar
      A diacritic combining two symbols into one phonological unit
      (e.g., /t͡s/). Used for :term:`affricates`. LatticeLang displays
      tie-bar forms canonically and accepts non-tie-bar input as
      aliases. See :ref:`adr-028`.

   tone
      Use of pitch to distinguish meaning at the word or morpheme level
      (e.g., Mandarin mā "mother" vs má "hemp"). LatticeLang provides
      options for tone-bearing units and a dedicated tone module.
      Post-MVP. See :ref:`constraint-types-overview`, :term:`suprasegmental`.

   tongue tip
   apex : anatomical
      The foremost point of the tongue. Articulations made with it
      are :term:`apical`; contrast :term:`laminal` (tongue blade).

   tongue root : anatomical
      The rearmost portion of the tongue, forming the front wall of
      the :term:`pharynx`. Its retraction (ATR) or constriction
      produces :term:`pharyngeal` sounds and distinguishes tongue-root
      vowel harmony systems, e.g., Akan.

   trill
   trills : manner of articulation
      Rapid vibration of an articulator (e.g., Spanish rolled /r/).
      High sonority.

   underlying form
   underlying forms
      The abstract, mental representation of a word's pronunciation
      before phonological rules apply. In generative phonology, the
      starting point for derivation. In LatticeLang, represented by
      the LanguageDefinition (inventory + templates + constraints).

   UniMorph
      A cross-linguistic morphological feature database providing
      standardized morphological features across languages. Potential
      future data source for LatticeLang's morphology module. See
      :ref:`q22-unimorph-integration`.

   universal dependencies
   UD
      A collaborative project providing consistent morphosyntactic
      annotation across ~200 languages. Its universal→override
      organizational pattern informs LatticeLang's architecture. See
      :ref:`q23-universal-override-model` and :cite:p:`ud2024`.

   universal → override model
      A design pattern where universal defaults are defined once, and
      language-specific or dialect-specific configurations override only
      what differs. Inspired by :term:`universal dependencies`. See
      :ref:`q23-universal-override-model`.

   unstressed
      A syllable that does not bear primary or secondary stress. Relevant
      for phonotactic variation — unstressed syllables often permit fewer
      consonant clusters. See :term:`prosody`.

   unrounded
      Said of a vowel or glide articulated without lip rounding
      — lips neutral or spread (/i e a/), as opposed to rounded
      (/u o/). The negative value of the [round] feature, which
      LatticeLang's ``harmony`` constraint can target; the
      rounded/unrounded pairing recurs in backness-harmony
      systems (Turkish pairs each back vowel with a rounded
      counterpart).

   uvular : place of articulation
      Tongue dorsum contacts the uvula. e.g., French /ʁ/, Arabic /q/.

   velar : place of articulation
      Tongue dorsum contacts the :term:`soft palate`. e.g., /k/, /ɡ/, /ŋ/.

   velarisation
   velarization : secondary articulation
      A :term:`secondary articulation` where the tongue body raises toward the
      :term:`velum` during another articulation. Mark - 	ˠ, e.g., English "dark l" /ɫ/.
      Velarization can also be a :term:`process` as a transformation or
      'historical process'.

   velum
   soft palate : anatomical
      The soft, movable rear portion of the roof of the mouth.
      Raised, it closes off the nasal cavity and produces oral
      sounds; lowered, air passes through the nose and produces
      nasal sounds (/m n ŋ/ and nasalized vowels). Hence the
      feature [nasal] is sometimes described as a "velum
      position" feature, and nasal harmony as movement of a
      raised/lowered velum setting across a domain.

   vocal fold
   vocal folds
   vocal cord
   vocal cords : anatomical
      Two folds of tissue in the :term:`larynx` whose vibration produces voicing.
      Voiced sounds have vibrating vocal folds; :term:`voiceless` sounds do not.

   voiced
   voicing
   vocal fold vibration
   laryngeal state
      Produced with vocal fold vibration. A binary feature:
      [+voice] or [-voice]. Distinguishes minimal pairs
      like /p/ (voiceless) vs /b/ (voiced). Specific
      to :term:`consonants`.

   voiceless
      Produced without :term:`vocal fold` vibration — the vocal
      folds are open or only loosely approximated. Roughly a
      third of the world's languages pair every stop this way:
      /p/ vs. /b/, /t/ vs. /d/, /s/ vs. /z/. Between voiced and
      voiceless lie partial states like intervocalic devoicing.
      See :term:`voicing`.

   vowel
   vowels
      A speech sound produced with an open vocal tract and no
      significant constriction. Characterized by height, backness,
      and rounding. Typically the :term:`nucleus` of a syllable.
      Determined by :term:`height`, :term:`backness`, and :term:`rounding`.

   vowel harmony
      A type of :term:`harmony` where vowels within a domain must share
      a feature (e.g., front/back in Finnish, rounded/unrounded in
      Turkish). Cross-syllable vowel harmony is post-MVP in LatticeLang.

   vowel sequence
     See :term:`hiatus`. The term emphasizes the material
     (vowels) rather than the syllabic structure.