"""Texts From Your Future Self — make.fun entry.

Brief (from the kit's RULES.txt): write ONE funny text message, under
200 characters, that the writer's future self sends back to them. It must
be funny by itself, with no setup and no context — just the message as it
would arrive. The house judge (a comedy editor) compares entries pairwise
and weighs, most important first:

  1. It IS a funny text message from the writer's future self, written
     as if sent back to the present self.
  2. It lands a real joke, with a twist or a flash of recognition that
     pays off by the last line.
  3. It sounds like a SPECIFIC future self, with a voice and details
     that could only come from that person's life.
  4. It uses the 200 characters well — no wasted words, punchline fast.
  5. It finds a fresh angle instead of the obvious joke about still
     being broke or still tired.

Craft of this line (why each part is here, in build order):

  * OPENER — "hey, it's me, you, from 2041." Lowercase, no greeting
    ceremony, a year far enough to be funny and near enough to sting.
    The little self-correction — "me, you" — is a comic beat in itself:
    the future self catches himself mid-sentence, which is exactly how
    a real text sounds. It establishes the future-self voice in eight
    words (criteria 1, 3): this is a text, not a letter, and the sender
    is unmistakably you.
  * FIRST DETAIL — "the robot vacuum unionized". A fresh angle
    (criterion 5): not broke, not tired — the dumb little appliance
    you bought to save time has organised against you. It is absurd,
    concrete, and instantly visual.
  * TWIST — "the houseplant you never watered is now your landlord".
    The payoff (criterion 2). The plant is the most personal detail in
    the line: only YOUR future self knows you never water it. The
    escalation — neglected plant to landlord — is the flash of
    recognition: your small daily neglects compound into a future where
    the things you ignored own you.
  * CLOSER — "and mom is still waiting on that reply." The human
    anchor. After two absurd images, one painfully ordinary truth
    lands the joke in real life: some things do not change in 15 years,
    and the most mundane one is the one that stings. It is also the
    most specific-to-a-life detail of all — every reader has a version
    of that unanswered message.

The whole message reads like a real text: lowercase, comma-spliced,
no wasted words, punchline at the end.
"""

import os

# --- The text, built from its meaningful parts (see the docstring) ---

# Future-self voice: a text, not a letter; the sender is you.
# The "me, you" self-correction is a small comic beat up front.
OPENER = "hey, it's me, you, from 2041. "

# Fresh angle: the appliance organised against you. Not broke, not tired.
DETAIL_ONE = "the robot vacuum unionized, "

# The twist: the plant you neglected now owns the place.
DETAIL_TWO = "the houseplant you never watered is now your landlord, "

# The human anchor: the one thing that never changes.
CLOSER = "and mom is still waiting on that reply."

ENTRY = OPENER + DETAIL_ONE + DETAIL_TWO + CLOSER

# Gate: the sealed scorer requires UTF-8 text of 1 to 200 characters,
# not only white space. Fail loudly here instead of shipping an
# invalid entry.
assert ENTRY.strip(), "entry must not be only white space"
assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)

print(f"{ENTRY}  [{len(ENTRY)} chars]")
