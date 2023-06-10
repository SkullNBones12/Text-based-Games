# Hangman attempt. Are all the words correct? Hopefully.

import random

print(""""
      Welcome to Hangman! Please choose a number between 
      3 && 12 for length of the word."""
      )
# List of words that will be chosen at random based on user input
threeLetters = [
    "aba", "abs", "ace", "act", "add", "ado", "aft", "age", "ago", "aha", "aid", "aim",
    "air", "ala", "ale", "all", "alt", "amp", "ana", "and", "ant", "any", "ape", "app",
    "apt", "arc", "are", "ark", "arm", "art", "ash", "ask", "asp", "ass", "ate", "ave",
    "awe", "axe", "aye", "BAA", "bad", "bag", "ban", "bar", "bat", "bay", "bed", "bee",
    "beg", "bel", "ben", "bet", "bid", "big", "bin", "bio", "bis", "bit", "biz", "bob",
    "bog", "boo", "bow", "box", "boy", "bra", "bud", "Bug", "bum", "bun", "bus", "but",
    "buy", "bye", "cab", "cad", "cam", "can", "cap", "car", "cat", "chi", "cob", "cod",
    "col", "con", "coo", "cop", "cor", "cos", "cot", "cow", "cox", "coy", "cry", "cub",
    "cue", "cup", "cut", "dab", "dad", "dal", "dam", "dan", "day", "Dee", "def", "del",
    "den", "dew", "did", "die", "dig", "dim", "din", "dip", "dis", "doc", "doe", "dog",
    "don", "dot", "dry", "dub", "due", "dug", "dun", "duo", "dye", "ear", "eat", "ebb",
    "ecu", "eft", "egg", "ego", "elf", "elm", "emu", "end", "era", "eta", "eve", "eye",
    "fab", "fad", "fan", "far", "fat", "fax", "fay", "fed", "fee", "fen", "few", "fig",
    "fin", "fir", "fit", "fix", "flu", "fly", "foe", "fog", "for", "fox", "fry", "fun",
    "fur", "gag", "gal", "gap", "gas", "gay", "gee", "gel", "gem", "get", "gig", "gin",
    "god", "got", "gum", "gun", "gut", "guy", "gym", "had", "ham", "has", "hat", "hay",
    "hem", "hen", "her", "hey", "hid", "him", "hip", "his", "hit", "hog", "hon", "hop",
    "hot", "how", "hub", "hue", "hug", "huh", "hum", "hut", "ice", "icy", "igg", "ill",
    "imp", "ink", "inn", "ion", "its", "ivy", "jam", "jar", "jaw", "jay", "jet", "jew",
    "job", "joe", "jog", "joy", "jug", "jun", "kay", "ken", "key", "kid", "kin", "kit",
    "lab", "lac", "lad", "lag", "lam", "lap", "law", "lax", "lay", "lea", "led", "Lee",
    "leg", "les", "let", "lib", "lid", "lie", "lip", "lit", "log", "lot", "low", "mac",
    "mad", "mag", "man", "map", "mar", "mas", "mat", "max", "may", "med", "meg", "men",
    "Met", "mid", "mil", "mix", "mob", "mod", "mol", "mom", "mon", "mop", "mot", "mud",
    "mug", "mum", "nab", "nah", "nan", "nap", "nay", "neb", "neg", "net", "new", "nil",
    "nip", "nod", "nor", "nos", "not", "now", "nun", "nut", "oak", "odd", "off", "oft",
    "oil", "old", "ole", "one", "ooh", "opt", "orb", "ore", "our", "out", "owe", "owl",
    "own", "pac", "pad", "pal", "pam", "pan", "pap", "par", "pas", "pat", "paw", "pay",
    "pea", "peg", "pen", "pep", "per", "pet", "pew", "phi", "pic", "pie", "pig", "pin",
    "pip", "pit", "ply", "pod", "pol", "pop", "pot", "pro", "psi", "pub", "pup", "put",
    "rad", "rag", "raj", "ram", "ran", "rap", "rat", "raw", "ray", "red", "ref", "reg",
    "rem", "rep", "rev", "rib", "rid", "rig", "rim", "rip", "rob", "rod", "roe", "rot",
    "row", "rub", "rue", "rug", "rum", "run", "rye", "sab", "sac", "sad", "sae", "sag",
    "sal", "sap", "sat", "saw", "say", "sea", "sec", "see", "sen", "set", "sew", "sex",
    "she", "shy", "sic", "sim", "sin", "sip", "sir", "sis", "sit", "six", "ski", "sky",
    "sly", "sod", "sol", "son", "sow", "soy", "spa", "spy", "sub", "sue", "sum", "sun",
    "sup", "tab", "tad", "tag", "tam", "tan", "tap", "tar", "tat", "tax", "tea", "ted",
    "tee", "ten", "the", "thy", "tie", "tin", "tip", "tod", "toe", "tom", "ton", "too",
    "top", "tor", "tot", "tow", "toy", "try", "tub", "tug", "two", "use", "van", "vat",
    "vet", "via", "vie", "vow", "wan", "war", "was", "wax", "way", "web", "wed", "wee",
    "wet", "who", "why", "wig", "win", "wis", "wit", "won", "woo", "wow", "wry", "wye",
    "yen", "yep", "yes", "yet", "you", "zip", "zoo"
]

fourLetters = [
    'Will', 'Wife', 'Wine', 'Wind', 'West', 'Word', 'Wood', 'Work', 'Year', 'Week',
    'Area', 'Army', 'Baby', 'Back', 'Ball', 'Band', 'Bank', 'Base', 'Bill', 'Body',
    'Book', 'Call', 'Card', 'Care', 'Case', 'Cash', 'City', 'Club', 'Cost', 'Date',
    'Deal', 'Door', 'Duty', 'East', 'Edge', 'Face', 'Fact', 'Farm', 'Fear', 'Fig',
    'File', 'Film', 'Fire', 'Firm', 'Fish', 'Food', 'Foot', 'Form', 'Fund', 'Game',
    'Girl', 'Goal', 'Gold', 'Hair', 'Half', 'Hall', 'Hand', 'Head', 'Help', 'Hill',
    'Home', 'Hope', 'Hour', 'Idea', 'Jack', 'John', 'Kind', 'King', 'Lack', 'Lady',
    'Land', 'Life', 'Line', 'List', 'Look', 'Lord', 'Loss', 'Love', 'Mark', 'Mary',
    'Mind', 'Miss', 'Move', 'Name', 'Need', 'News', 'Note', 'Page', 'Pain', 'Pair',
    'Park', 'Part', 'Past', 'Path', 'Paul', 'Plan', 'Play', 'Post', 'Race', 'Rain',
    'Rate', 'Rest', 'Rise', 'Risk', 'Road', 'Rock', 'Role', 'Room', 'Rule', 'Sale',
    'Seat', 'Shop', 'Show', 'Side', 'Sign', 'Site', 'Size', 'Skin', 'Sort', 'Star',
    'Step', 'Task', 'Team', 'Term', 'Test', 'Text', 'Time', 'Tour', 'Town', 'Tree',
    'Turn', 'Type', 'Unit', 'User', 'View', 'Dese', 'Enuf', 'Feel', 'Hern', 'Hers',
    'Many', 'Mine', 'Mine', 'Much', 'Nada', 'Nish', 'None', 'Nowt', 'Ours', 'Same',
    'Self', 'Some', 'Such', 'That', 'Thee', 'Them', 'They', 'This', 'Thon', 'Thor',
    'Thou', 'Thou', 'Tone', 'What', 'Yere', 'Your', 'Will', 'Roll', 'Tend', 'Miss',
    'Vote', 'Have', 'Earn', 'Give', 'Bear', 'Step', 'Look', 'Call', 'Risk', 'Love',
    'Rest', 'Warn', 'Help', 'Pass', 'Hold', 'Find', 'Walk', 'Save', 'Sing', 'Need',
    'Face', 'Lift', 'Cope', 'Cook', 'Link', 'Shed', 'Join', 'Show', 'Cast', 'Pray',
    'Wish', 'Want', 'Know', 'Make', 'Mind', 'Slip', 'Take', 'Sign', 'Fill', 'Fail',
    'View', 'Gain', 'Lose', 'Talk', 'Hate', 'Grow', 'Seem', 'Come', 'Form', 'Draw', 
    'Land', 'Suit', 'Wait', 'Sell', 'Care', 'Rule', 'Read', 'Jump', 'Hide', 'Plan',
    'Work', 'Send', 'Ring', 'Wear', 'Pick', 'Deny', 'Name', 'Push', 'Note', 'Burn',
    'Live', 'Must', 'Mark', 'Ride', 'Feel', 'Last', 'Kill', 'Pull', 'Hang', 'Test',
    'Tell', 'Beat', 'Meet', 'Fall', 'Turn', 'Stay', 'Stop', 'Wash', 'Keep', 'Rise',
    'Shut', 'Like', 'Deal', 'Open', 'Seek', 'Vary', 'Play', 'Rely', 'Fear', 'Hurt',
    'Wake', 'Cost', 'Hear', 'Head', 'Lead', 'Sort', 'Lend', 'Dare', 'Drop', 'Blow',
    'Hope', 'Full', 'Neat', 'Grim', 'Mass', 'Deaf', 'Cold', 'Huge', 'Bare', 'Mild',
    'Firm', 'Dual', 'Okay', 'Fine', 'Just', 'Able', 'Glad', 'Easy', 'Mean', 'Bold',
    'Flat', 'Pink', 'Dark', 'Next', 'Main', 'Male', 'Last', 'Back', 'Dead', 'Damp',
    'Calm', 'Lazy', 'Hard', 'Only', 'Lone', 'Head', 'Poor', 'Late', 'Open', 'Like',
    'Loud', 'Keen', 'Holy', 'Evil', 'Mere', 'Bass', 'High', 'Blue', 'Dull', 'Live',
    'Pale', 'Fond', 'Fair', 'Foul', 'Long', 'Nazi', 'Past', 'Kind', 'Busy', 'Cool',
    'Near', 'Good', 'Oral', 'Dear', 'Half', 'Fast', 'Dumb', 'Nice', 'Deep', 'Grey',
    'Free', 'Pure', 'Rare', 'Real', 'Rear', 'Rich', 'Rude', 'Safe', 'Same', 'Sick',
    'Slim', 'Slow', 'Soft', 'Sole', 'Sore', 'Sure', 'Tall', 'Then', 'Thin', 'Tidy',
    'Tiny', 'Tory', 'True', 'Ugly', 'Vain', 'Vast', 'Very', 'Vice', 'Warm', 'Wary',
    'Weak', 'Wide', 'Wild', 'Wise', 'Zero', 'Thou', 'Till', 'When', 'Sith', 'Only',
    'Once', 'Plus', 'That', 'Save', 'Lest', 'Both', 'Like', 'Than', 'Unto', 'Then',
    'Ergo', 'Else'
]

fiveLetters = [
    'About', 'Alert', 'Argue', 'Beach', 'Above', 'Alike', 'Arise', 'Began',
    'Abuse', 'Alive', 'Array', 'Begin', 'Actor', 'Allow', 'Aside', 'Begun',
    'Acute', 'Alone', 'Asset', 'Being', 'Admit', 'Along', 'Audio', 'Below',
    'Adopt', 'Alter', 'Audit', 'Bench', 'Adult', 'Among', 'Avoid', 'Billy',
    'After', 'Anger', 'Award', 'Birth', 'Again', 'Angle', 'Aware', 'Black',
    'Agent', 'Angry', 'Badly', 'Blame', 'Agree', 'Apart', 'Baker', 'Blind',
    'Ahead', 'Apple', 'Bases', 'Block', 'Alarm', 'Apply', 'Basic', 'Blood',
    'Album', 'Arena', 'Basis', 'Board', 'Boost', 'Buyer', 'China', 'Cover',
    'Booth', 'Cable', 'Chose', 'Craft', 'Bound', 'Calif', 'Civil', 'Crash',
    'Brain', 'Carry', 'Claim', 'Cream', 'Brand', 'Catch', 'Class', 'Crime',
    'Bread', 'Cause', 'Clean', 'Cross', 'Break', 'Chain', 'Clear', 'Crowd',
    'Breed', 'Chair', 'Click', 'Crown', 'Brief', 'Chart', 'Clock', 'Curve',
    'Bring', 'Chase', 'Close', 'Cycle', 'Broad', 'Cheap', 'Coach', 'Daily',
    'Broke', 'Check', 'Coast', 'Dance', 'Brown', 'Chest', 'Could', 'Dated',
    'Build', 'Chief', 'Count', 'Dealt', 'Built', 'Child', 'Court', 'Death',
    'Debut', 'Entry', 'Forth', 'Group', 'Delay', 'Equal', 'Forty', 'Grown',
    'Depth', 'Error', 'Forum', 'Guard', 'Doing', 'Event', 'Found', 'Guess',
    'Doubt', 'Every', 'Frame', 'Guest', 'Dozen', 'Exact', 'Frank', 'Guide',
    'Draft', 'Exist', 'Fraud', 'Happy', 'Drama', 'Extra', 'Fresh', 'Harry',
    'Drawn', 'Faith', 'Front', 'Heart', 'Dream', 'False', 'Fruit', 'Heavy',
    'Dress', 'Fault', 'Fully', 'Hence', 'Drill', 'Fiber', 'Funny', 'Night',
    'Drink', 'Field', 'Giant', 'Horse', 'Drive', 'Fifth', 'Given', 'Hotel',
    'Drove', 'Fifty', 'Glass', 'House', 'Dying', 'Fight', 'Globe', 'Human',
    'Eager', 'Final', 'Going', 'Ideal', 'Early', 'First', 'Grace', 'Image',
    'Earth', 'Fixed', 'Grade', 'Index', 'Eight', 'Flash', 'Grand', 'Inner',
    'Elite', 'Fleet', 'Grant', 'Input', 'Empty', 'Floor', 'Grass', 'Issue',
    'Enemy', 'Fluid', 'Great', 'Irony', 'Enjoy', 'Focus', 'Green', 'Juice',
    'Enter', 'Force', 'Gross', 'Joint', 'Judge', 'Metal', 'Media', 'Newly',
    'Known', 'Local', 'Might', 'Noise', 'Label', 'Logic', 'Minor', 'North',
    'Large', 'Loose', 'Minus', 'Noted', 'Laser', 'Lower', 'Mixed', 'Novel',
    'Later', 'Lucky', 'Model', 'Nurse', 'Laugh', 'Lunch', 'Money', 'Occur',
    'Layer', 'Lying', 'Month', 'Ocean', 'Learn', 'Magic', 'Moral', 'Offer',
    'Lease', 'Major', 'Motor', 'Often', 'Least', 'Maker', 'Mount', 'Order',
    'Leave', 'March', 'Mouse', 'Other', 'Legal', 'Music', 'Mouth', 'Ought',
    'Level', 'Match', 'Movie', 'Paint', 'Light', 'Mayor', 'Needs', 'Paper',
    'Limit', 'Meant', 'Never', 'Party', 'Peace', 'Power', 'Radio', 'Round',
    'Panel', 'Press', 'Raise', 'Route', 'Phase', 'Price', 'Range', 'Royal',
    'Phone', 'Pride', 'Rapid', 'Rural', 'Photo', 'Prime', 'Ratio', 'Scale',
    'Piece', 'Print', 'Reach', 'Scene', 'Pilot', 'Prior', 'Ready', 'Scope',
    'Pitch', 'Prize', 'Refer', 'Score', 'Place', 'Proof', 'Right', 'Sense',
    'Plain', 'Proud', 'Rival', 'Serve', 'Plane', 'Prove', 'River', 'Seven',
    'Plant', 'Queen', 'Quick', 'Shall', 'Plate', 'Sixth', 'Stand', 'Shape',
    'Point', 'Quiet', 'Roman', 'Share', 'Pound', 'Quite', 'Rough', 'Sharp',
    'Sheet', 'Spare', 'Style', 'Times', 'Shelf', 'Speak', 'Sugar', 'Tired',
    'Shell', 'Speed', 'Suite', 'Title', 'Shift', 'Spend', 'Super', 'Today',
    'Shirt', 'Spent', 'Sweet', 'Topic', 'Shock', 'Split', 'Table', 'Total',
    'Shoot', 'Spoke', 'Taken', 'Touch', 'Short', 'Sport', 'Taste', 'Tough',
    'Shown', 'Staff', 'Taxes', 'Tower', 'Sight', 'Stage', 'Teach', 'Track',
    'Since', 'Stake', 'Teeth', 'Trade', 'Sixty', 'Start', 'Texas', 'Treat',
    'Sized', 'State', 'Thank', 'Trend', 'Skill', 'Steam', 'Theft', 'Trial',
    'Sleep', 'Steel', 'Their', 'Tried', 'Slide', 'Stick', 'Theme', 'Tries',
    'Small', 'Still', 'There', 'Truck', 'Smart', 'Stock', 'These', 'Truly',
    'Smile', 'Stone', 'Thick', 'Trust', 'Smith', 'Stood', 'Thing', 'Truth',
    'Smoke', 'Store', 'Think', 'Twice', 'Solid', 'Storm', 'Third', 'Under',
    'Solve', 'Story', 'Those', 'Undue', 'Sorry', 'Strip', 'Three', 'Union',
    'Sound', 'Stuck', 'Threw', 'Unity', 'South', 'Study', 'Throw', 'Until',
    'Space', 'Stuff', 'Tight', 'Upper', 'Upset', 'Whole', 'Waste', 'Wound',
    'Urban', 'Whose', 'Watch', 'Write', 'Usage', 'Woman', 'Water', 'Wrong',
    'Usual', 'Train', 'Wheel', 'Wrote', 'Valid', 'World', 'Where', 'Yield',
    'Value', 'Worry', 'Which', 'Young', 'Video', 'Worse', 'While', 'Youth',
    'Virus', 'Worst', 'White', 'Worth', 'Visit', 'Would', 'Vital', 'Voice'
]

sixLetters = [
    'Animal', 'Basket', 'Bubble', 'Butter', 'Camera', 'Carpet', 'Castle', 'Cheese',
    'Danger', 'Dragon', 'Father', 'Flower', 'Forest', 'Guitar', 'Jungle', 'Mother',
    'Orange', 'Pepper', 'Pillow', 'Planet', 'Potato', 'Rocket', 'Sailor', 'Shadow',
    'Spirit', 'Sunset', 'Tomato', 'Turtle', 'Window', 'Winter', 'Course', 'System',
    'School', 'Family', 'Market', 'Police', 'Policy', 'Office', 'Person', 'Health',
    'Period', 'Centre', 'Effect', 'Action', 'Moment', 'Report', 'Church', 'Change',
    'Street', 'Result', 'Reason', 'Nature', 'Member', 'Figure', 'Friend', 'Amount',
    'Series', 'Future', 'Labour', 'Letter', 'Theory', 'Growth', 'Chance', 'Record',
    'Energy', 'Income', 'Scheme', 'Design', 'Choice', 'Couple', 'County', 'Summer',
    'Colour', 'Season', 'Garden', 'Charge', 'Advice', 'Doctor', 'Extent', 'Access',
    'Region', 'Degree', 'Return', 'Public', 'Answer', 'Leader', 'Appeal', 'Method',
    'Source', 'Oxford', 'Demand', 'Sector', 'Status', 'Safety', 'Weight', 'League',
    'Budget', 'Review', 'Minute', 'Survey', 'Speech', 'Effort', 'Career', 'Attack',
    'Length', 'Memory', 'Impact', 'Sister', 'Corner', 'Damage', 'Credit', 'Debate',
    'Supply', 'Museum', 'Island', 'Relief', 'Target', 'Coffee', 'Factor', 'Battle',
    'Prison', 'Bridge', 'Detail', 'Client', 'Search', 'Master', 'Dinner', 'Agency',
    'Manner', 'Favour', 'Crisis', 'Prince', 'Output', 'Middle', 'Player', 'Threat',
    'Notice', 'Bottom', 'Profit', 'Second', 'Option', 'Reform', 'Spring', 'Estate',
    'Volume', 'Martin', 'Branch', 'Object', 'Driver', 'Belief', 'Murder', 'Flight',
    'Treaty', 'Desire', 'Palace', 'Engine', 'Breath', 'Screen', 'Silver', 'Injury',
    'Valley', 'Should', 'Become', 'Change', 'Appear', 'Expect', 'Ensure', 'Follow',
    'Accept', 'Remain', 'Happen', 'Create', 'Return', 'Reduce', 'Choose', 'Decide',
    'Forget', 'Listen', 'Answer', 'Enable', 'Affect', 'Obtain', 'Spread', 'Wonder',
    'Afford', 'Regard', 'Assume', 'Manage', 'Remove', 'Prefer', 'Travel', 'Attend',
    'Depend', 'Suffer', 'Notice', 'Result', 'Extend', 'Report', 'Arrive', 'Finish',
    'Secure', 'Escape', 'Assess', 'Repeat', 'Supply', 'Reveal', 'Relate', 'Retain',
    'Handle', 'Assist', 'Recall', 'Settle', 'Ignore', 'Define', 'Record', 'Bother',
    'Refuse', 'Demand', 'Reckon', 'Belong', 'Emerge', 'Intend', 'Advise', 'Defend',
    'Pursue', 'Resist', 'Impose', 'Appeal', 'Differ', 'Select', 'Attack', 'Expand',
    'Behave', 'Strike', 'Remind', 'Review', 'Employ', 'Insist', 'Switch', 'Invest',
    'Tackle', 'Gather', 'Reject', 'Inform', 'Borrow', 'Comply', 'Permit', 'Charge',
    'Commit', 'Detect', 'Excuse', 'Damage', 'Launch', 'Direct', 'Submit', 'Invite',
    'Divide', 'Engage', 'Search', 'Fulfil', 'Convey', 'Market', 'Thrust', 'Retire',
    'Adjust', 'Exceed', 'Occupy', 'Stress', 'Object', 'Please', 'Design', 'Resign',
    'Regret', 'Offset', 'Assure', 'Derive', 'Access', 'Favour', 'Cancel', 'Oppose',
    'Locate', 'Repair', 'Amount', 'Attach', 'Absorb', 'Admire', 'Combat', 'Update',
    'Modify', 'Resume', 'Render', 'Double', 'Assert', 'Defeat', 'Wander', 'Rescue',
    'Export', 'Induce', 'Figure', 'Regain', 'Devote', 'Devise', 'Govern', 'Expose',
    'Beware', 'Arrest', 'Effect', 'Murder', 'Freeze', 'Honour', 'Revive', 'Endure',
    'Insert', 'Evolve', 'Foster', 'Reform', 'Punish', 'Little', 'Social', 'Second',
    'Public', 'Likely', 'Common', 'Single', 'Former', 'Recent', 'Strong', 'Simple',
    'Modern', 'Normal', 'Soviet', 'Direct', 'Useful', 'German', 'Future', 'Senior',
    'Annual', 'Latter', 'Active', 'Middle', 'Sexual', 'Actual', 'Famous', 'Formal',
    'Proper', 'Unable', 'Lovely', 'Fourth', 'Female', 'Mental', 'Double', 'Afraid',
    'Bright', 'Bloody', 'Narrow', 'Entire', 'Severe', 'Unique', 'Guilty', 'Yellow',
    'Golden', 'Sudden', 'Global', 'Silent', 'Secret', 'Visual', 'Wooden', 'Stupid',
    'Stable', 'Honest', 'Slight', 'Remote', 'Gentle', 'Junior', 'Smooth', 'Pretty',
    'Fellow', 'Square', 'Steady', 'Bitter', 'Ethnic', 'Weekly', 'Random', 'Modest',
    'Asleep', 'Clever', 'Liable', 'Mutual', 'Nearby', 'Urgent', 'Superb', 'Strict',
    'Marine', 'Retail', 'Unfair', 'Hungry', 'Secure', 'Subtle', 'Decent', 'Bottom',
    'Lesser', 'Casual', 'Lonely', 'Fierce', 'Verbal', 'Mature', 'Absent', 'Racial',
    'Lively', 'Mobile', 'Linear', 'Orange', 'Fiscal', 'Tender', 'Eighth', 'Liquid',
    'Sacred', 'Worthy', 'Manual', 'Divine', 'Intact', 'Select', 'Tragic', 'Inland',
    'Gothic', 'Tribal', 'Ironic', 'Robust', 'Binary', 'Scarce', 'Uneven', 'Unlike',
    'Latent', 'Lethal', 'Gloomy', 'Filthy', 'Serial', 'Tricky', 'Hollow', 'Finite',
    'Coarse', 'Median', 'Baltic', 'Savage', 'Glossy', 'Racist', 'Dental', 'Inward',
    'Foster', 'Unsure', 'Feudal', 'Unpaid', 'Heroic', 'Distal', 'Inside', 'Upward',
    'Aerial', 'Triple', 'Exempt', 'Facial', 'Ritual', 'Faulty', 'Speedy', 'Lawful',
    'Floppy', 'Neural', 'Shrewd', 'Lavish', 'Rectal', 'Floral', 'Hectic', 'Arable',
    'Erotic', 'Feeble', 'Sleepy', 'Innate', 'Dorsal', 'Spinal', 'Dismal', 'Barren',
    'Meagre', 'Shabby', 'Banana', 'Bumble', 'Cactus', 'Dabble', 'Fluffy', 'Giggly',
    'Hiccup', 'Jester', 'Kaboom', 'Muppet', 'Noodle', 'Pajama', 'Quirky', 'Scooby',
    'Tickle', 'Waffle', 'Yippee', 'Zipper', 'Zoodle', 'Boogie', 'Chubby', 'Doodle',
    'Fizzle', 'Goofus', 'Hookey', 'Jumble', 'Kookie', 'Lively', 'Muddle', 'Nutmeg',
    'Puddle', 'Quacky', 'Razzle', 'Sizzle', 'Tootle', 'Wiggly', 'Yabber', 'Zephyr',
    'Zonked'
]

sevenLetters = [
    'ability', 'absence', 'academy', 'account', 'accused', 'achieve',
    'acquire', 'address', 'advance', 'adverse', 'advised', 'adviser',
    'against', 'airline', 'airport', 'alcohol', 'alleged', 'already',
    'analyst', 'ancient', 'another', 'anxiety', 'anxious', 'anybody',
    'applied', 'arrange', 'arrival', 'article', 'assault', 'assumed',
    'assured', 'attempt', 'attract', 'auction', 'average', 'backing',
    'balance', 'banking', 'barrier', 'battery', 'bearing', 'beating',
    'because', 'bedroom', 'believe', 'beneath', 'benefit', 'besides',
    'between', 'billion', 'binding', 'brother', 'brought', 'burning',
    'cabinet', 'caliber', 'calling', 'capable', 'capital', 'captain',
    'caption', 'capture', 'careful', 'carrier', 'caution', 'ceiling',
    'central', 'centric', 'century', 'certain', 'chamber', 'channel',
    'chapter', 'charity', 'charlie', 'charter', 'checked', 'chicken',
    'chronic', 'circuit', 'classes', 'classic', 'climate', 'closing',
    'closure', 'clothes', 'collect', 'college', 'combine', 'comfort',
    'command', 'comment', 'compact', 'company', 'compare', 'compete',
    'complex', 'concept', 'concern', 'concert', 'conduct', 'confirm',
    'connect', 'consent', 'consist', 'contact', 'contain', 'content',
    'contest', 'context', 'control', 'convert', 'correct', 'council',
    'counsel', 'counter', 'country', 'crucial', 'crystal', 'culture',
    'current', 'cutting', 'dealing', 'decided', 'decline', 'default',
    'defence', 'deficit', 'deliver', 'density', 'deposit', 'desktop',
    'despite', 'destroy', 'develop', 'devoted', 'diamond', 'digital',
    'discuss', 'disease', 'display', 'dispute', 'distant', 'diverse',
    'divided', 'drawing', 'driving', 'dynamic', 'eastern', 'economy',
    'edition', 'elderly', 'element', 'engaged', 'enhance', 'essence',
    'evening', 'evident', 'exactly', 'examine', 'example', 'excited',
    'exclude', 'exhibit', 'expense', 'explain', 'explore', 'express',
    'extreme', 'factory', 'faculty', 'failing', 'failure', 'fashion',
    'feature', 'federal', 'feeling', 'fiction', 'fifteen', 'filling',
    'finance', 'finding', 'fishing', 'fitness', 'foreign', 'forever',
    'formula', 'fortune', 'forward', 'founder', 'freedom', 'further',
    'gallery', 'gateway', 'general', 'genetic', 'genuine', 'gigabit',
    'greater', 'hanging', 'heading', 'healthy', 'hearing', 'heavily',
    'helpful', 'helping', 'herself', 'highway', 'himself', 'history',
    'holding', 'holiday', 'housing', 'however', 'hundred', 'husband',
    'illegal', 'illness', 'imagine', 'imaging', 'improve', 'include',
    'initial', 'inquiry', 'insight', 'install', 'instant', 'instead',
    'intense', 'interim', 'involve', 'jointly', 'journal', 'journey',
    'justice', 'justify', 'keeping', 'killing', 'kingdom', 'kitchen',
    'knowing', 'landing', 'largely', 'lasting', 'leading', 'learned',
    'leisure', 'liberal', 'liberty', 'library', 'license', 'limited',
    'listing', 'logical', 'loyalty', 'machine', 'manager', 'married',
    'massive', 'maximum', 'meaning', 'measure', 'medical', 'meeting',
    'mention', 'message', 'million', 'mineral', 'minimal', 'minimum',
    'missing', 'mission', 'mistake', 'mixture', 'monitor', 'monthly',
    'morning', 'musical', 'mystery', 'natural', 'neither', 'nervous',
    'network', 'neutral', 'notable', 'nothing', 'nowhere', 'nuclear',
    'nursing', 'obvious', 'offense', 'officer', 'ongoing', 'opening',
    'operate', 'opinion', 'optical', 'organic', 'outcome', 'outdoor',
    'outlook', 'outside', 'overall', 'pacific', 'package', 'painted',
    'parking', 'partial', 'partner', 'passage', 'passing', 'passion',
    'passive', 'patient', 'pattern', 'payable', 'payment', 'penalty',
    'pending', 'pension', 'percent', 'perfect', 'perform', 'perhaps',
    'phoenix', 'picking', 'picture', 'pioneer', 'plastic', 'pointed',
    'popular', 'portion', 'poverty', 'precise', 'predict', 'premier',
    'premium', 'prepare', 'present', 'prevent', 'primary', 'printer',
    'privacy', 'private', 'problem', 'proceed', 'process', 'produce',
    'product', 'profile', 'program', 'project', 'promise', 'promote',
    'protect', 'protein', 'protest', 'provide', 'publish', 'purpose',
    'pushing', 'qualify', 'quality', 'quarter', 'radical', 'railway',
    'readily', 'Reading', 'reality', 'realize', 'receipt', 'receive',
    'recover', 'reflect', 'regular', 'related', 'release', 'remains',
    'removal', 'removed', 'replace', 'request', 'require', 'reserve',
    'resolve', 'respect', 'respond', 'restore', 'retired', 'revenue',
    'reverse', 'rollout', 'routine', 'running', 'satisfy', 'science',
    'section', 'segment', 'serious', 'service', 'serving', 'session',
    'setting', 'seventh', 'several', 'shortly', 'showing', 'silence',
    'silicon', 'similar', 'sitting', 'sixteen', 'skilled', 'smoking',
    'society', 'somehow', 'someone', 'speaker', 'special', 'species',
    'sponsor', 'station', 'storage', 'strange', 'stretch', 'student',
    'studied', 'subject', 'succeed', 'success', 'suggest', 'summary',
    'support', 'suppose', 'supreme', 'surface', 'surgery', 'surplus',
    'survive', 'suspect', 'sustain', 'teacher', 'telecom', 'telling',
    'tension', 'theatre', 'therapy', 'thereby', 'thought', 'through',
    'tonight', 'totally', 'touched', 'towards', 'traffic', 'trouble',
    'turning', 'typical', 'uniform', 'unknown', 'unusual', 'upgrade',
    'upscale', 'utility', 'variety', 'various', 'vehicle', 'venture',
    'version', 'veteran', 'victory', 'viewing', 'village', 'violent',
    'virtual', 'visible', 'waiting', 'walking', 'wanting', 'warning',
    'warrant', 'wearing', 'weather', 'webcast', 'website', 'wedding',
    'weekend', 'welcome', 'welfare', 'western', 'whereas', 'whereby',
    'whether', 'willing', 'winning', 'without', 'witness', 'working',
    'writing', 'written'
]

eightLetters =[
    'ability',    'absence',    'academy',    'account',    'accused',    'achieve',    'acquire',
    'address',    'advance',    'adverse',    'advised',    'adviser',    'against',    'airline',
    'airport',    'alcohol',    'alleged',    'already',    'analyst',    'ancient',    'another',
    'anxiety',    'anxious',    'anybody',    'applied',    'arrange',    'arrival',    'article',
    'assault',    'assumed',    'assured',    'attempt',    'attract',    'auction',    'average',
    'backing',    'balance',    'banking',    'barrier',    'battery',    'bearing',    'beating',
    'because',    'bedroom',    'believe',    'beneath',    'benefit',    'besides',    'between',
    'billion',    'binding',    'brother',    'brought',    'burning',    'cabinet',    'caliber',
    'calling',    'capable',    'capital',    'captain',    'caption',    'capture',    'careful',
    'carrier',    'caution',    'ceiling',    'central',    'centric',    'century',    'certain',
    'chamber',    'channel',    'chapter',    'charity',    'charlie',    'charter',    'checked',
    'chicken',    'chronic',    'circuit',    'classes',    'classic',    'climate',    'closing',
    'closure',    'clothes',    'collect',    'college',    'combine',    'comfort',    'command',
    'comment',    'compact',    'company',    'compare',    'compete',    'complex',    'concept',
    'concern',    'concert',    'conduct',    'confirm',    'connect',    'consent',    'consist',
    'contact',    'contain',    'content',    'contest',    'context',    'control',    'convert',
    'correct',    'council',    'counsel',    'counter',    'country',    'crucial',    'crystal',
    'culture',    'current',    'cutting',    'dealing',    'decided',    'decline',    'default',
    'defence',    'deficit',    'deliver',    'density',    'deposit',    'desktop',    'despite',
    'destroy',    'develop',    'devoted',    'diamond',    'digital',    'discuss',    'disease',
    'display',    'dispute',    'distant',    'diverse',    'divided',    'drawing',    'driving',
    'dynamic',    'eastern',    'economy',    'edition',    'elderly',    'element',    'engaged',
    'enhance',    'essence',    'evening',    'evident',    'exactly',    'examine',    'example',
    'excited',    'exclude',    'exhibit',    'expense',    'explain',    'explore',    'express',
    'extreme',    'factory',    'faculty',    'failing',    'failure',    'fashion',    'feature',
    'federal',    'feeling',    'fiction',    'fifteen',    'filling',    'finance',    'finding',
    'fishing',    'fitness',    'foreign',    'forever',    'formula',    'fortune',    'forward',
    'founder',    'freedom',    'further',    'gallery',    'gateway',    'general',    'genetic',
    'genuine',    'gigabit',    'greater',    'hanging',    'heading',    'healthy',    'hearing',
    'heavily',    'helpful',    'helping',    'herself',    'highway',    'himself',    'history',
    'holding',    'holiday',    'housing',    'however',    'hundred',    'husband',    'illegal',
    'illness',    'imagine',    'imaging',    'improve',    'include',    'initial',    'inquiry',
    'insight',    'install',    'instant',    'instead',    'intense',    'interim',    'involve',
    'jointly',    'journal',    'journey',    'justice',    'justify',    'keeping',    'killing',
    'kingdom',    'kitchen',    'knowing',    'landing',    'largely',    'lasting',    'leading',
    'learned',    'leisure',    'liberal',    'liberty',    'library',    'license',    'limited',
    'listing',    'logical',    'loyalty',    'machine',    'manager',    'married',    'massive',
    'maximum',    'meaning',    'measure',    'medical',    'meeting',    'mention',    'message',
    'million',    'mineral',    'minimal',    'minimum',    'missing',    'mission',    'mistake',
    'mixture',    'monitor',    'monthly',    'morning',    'musical',    'mystery',    'natural',
    'neither',    'nervous',    'network',    'neutral',    'notable',    'nothing',    'nowhere',
    'nuclear',    'nursing',    'obvious',    'offense',    'officer',    'ongoing',    'opening',
    'operate',    'opinion',    'optical',    'organic',    'outcome',    'outdoor',    'outlook',
    'outside',    'overall',    'pacific',    'package',    'painted',    'parking',    'partial',
    'partner',    'passage',    'passing',    'passion',    'passive',    'patient',    'pattern',
    'payable',    'payment',    'penalty',    'pending',    'pension',    'percent',    'perfect',
    'perform',    'perhaps',    'phoenix',    'picking',    'picture',    'pioneer',    'plastic',
    'pointed',    'popular',    'portion',    'poverty',    'precise',    'predict',    'premier',
    'premium',    'prepare',    'present',    'prevent',    'primary',    'printer',    'privacy',
    'private',    'problem',    'proceed',    'process',    'produce',    'product',    'profile',
    'program',    'project',    'promise',    'promote',    'protect',    'protein',    'protest',
    'provide',    'publish',    'purpose',    'pushing',    'qualify',    'quality',    'quarter',
    'radical',    'railway',    'readily',    'Reading',    'reality',    'realize',    'receipt',
    'receive',    'recover',    'reflect',    'regular',    'related',    'release',    'remains',
    'removal',    'removed',    'replace',    'request',    'require',    'reserve',    'resolve',
    'respect',    'respond',    'restore',    'retired',    'revenue',    'reverse',    'rollout',
    'routine',    'running',    'satisfy',    'science',    'section',    'segment',    'serious',
    'service',    'serving',    'session',    'setting',    'seventh',    'several',    'shortly',
    'showing',    'silence',    'silicon',    'similar',    'sitting',    'sixteen',    'skilled',
    'smoking',    'society',    'somehow',    'someone',    'speaker',    'special',    'species',
    'sponsor',    'station',    'storage',    'strange',    'stretch',    'student',    'studied',
    'subject',    'succeed',    'success',    'suggest',    'summary',    'support',    'suppose',
    'supreme',    'surface',    'surgery',    'surplus',    'survive',    'suspect',    'sustain',
    'teacher',    'telecom',    'telling',    'tension',    'theatre',    'therapy',
    'thereby',    'thought',    'through',    'tonight',    'totally',    'touched',    'towards',
    'traffic',    'trouble',    'turning',    'typical',    'uniform',    'unknown',    'unusual',
    'upgrade',    'upscale',    'utility',    'variety',    'various',    'vehicle',    'venture',
    'version',    'veteran',    'victory',    'viewing',    'village',    'violent',    'virtual',
    'visible',    'waiting',    'walking',    'wanting',    'warning',    'warrant',    'wearing',
    'weather',    'webcast',    'website',    'wedding',    'weekend',    'welcome',    'welfare',
    'western',    'whereas',    'whereby',    'whether',    'willing',    'winning',    'without',
    'witness',    'working',    'writing',    'written'       
]

nineLetters = [
    'ACENTRICS', 'ACICLOVIR', 'ACULEATES', 'AEROSPIKE', 'AIRBOARDS', 'AIRPROXES', 'ALLODYNIA', 'ALPHATEST', 'ANIRIDIAS', 'ANTISHAKE', 'ANTPITTAS', 'ARCHDRUID',
    'ARCHSTONE', 'ARCMINUTE', 'ARSEHOLED', 'ARTHOUSES', 'ASHTANGAS', 'AUTOMAGIC', 'AUTOREPLY', 'AUTOSAVED', 'AUTOSAVES', 'AUTOTESTS', 'AVOPARCIN', 'AZYGOUSLY',
    'BACKPLATE', 'BANDEIRAS', 'BAROTITIS', 'BASHMENTS', 'BASSLINES', 'BATTLEAXE', 'BAZZAZZES', 'BEAKERFUL', 'BEATBOXER', 'BEJESUSES', 'BHELPURIS', 'BIOENERGY',
    'BIRDSFOOT', 'BISPHENOL', 'BLEOMYCIN', 'BLINGIEST', 'BLOCKSHIP', 'BLOGRINGS', 'BLOGROLLS', 'BLOOTERED', 'BOERBULLS', 'BOLOGNESE', 'BONETIRED', 'BOOGALOOS',
    'BOTTARGAS', 'BOYSHORTS', 'BRAINFOOD', 'BREADIEST', 'BRESAOLAS', 'BRISKIEST', 'BROTHIEST', 'BROWNTAIL', 'BULLYCIDE', 'BUPROPION', 'BUZZBAITS', 'BUZZKILLS',
    'CAIRNIEST', 'CALIMOCHO', 'CALLTIMES', 'CALMSTANE', 'CAMPEACHY', 'CAMPERIES', 'CAMPHONES', 'CANCELBOT', 'CANEGRUBS', 'CAREWARES', 'CARPHONES', 'CARSHARED',
    'CARSHARES', 'CASEMIXES', 'CASEVACED', 'CATAPHORS', 'CAUMSTANE', 'CECROPINS', 'CELECOXIB', 'CERCOPIDS', 'CETUXIMAB', 'CEVITAMIC', 'CHACONINE', 'CHAMPIEST',
    'CHANTINGS', 'CHAVVIEST', 'CHECKIEST', 'CHEQUIEST', 'CHERMOULA', 'CHIMINEAS', 'CHUMASHIM', 'CLOWNFISH', 'COACHIEST', 'COCKLINGS', 'COFIRINGS', 'COMBOVERS',
    'CONSPUING', 'COPYFIGHT', 'CRANACHAN', 'CRESSIEST', 'CROREPATI', 'CRUCIATES', 'CURVINESS', 'CYCLEPATH', 'DANCICALS', 'DARKFIELD', 'DATAGRAMS', 'DAYSAILER',
    'DAYSAILOR', 'DEMOSCENE', 'DEPIGMENT', 'DEQUEUING', 'DESEEDING', 'DETANGLED', 'DETANGLER', 'DETANGLES', 'DETRUSORS', 'DIGIPACKS', 'DIPSWITCH', 'DISABLISM',
    'DISABLIST', 'DISINVENT', 'DITHIONIC', 'DOCUSOAPS', 'DONEPEZIL', 'DOORNBOOM', 'DOUGHBALL', 'DOWELINGS', 'DOWNSIZER', 'DOXAPRAMS', 'DOXASTICS', 'DRAGGINGS',
    'DREIGHEST', 'DRILLHOLE', 'DUMBSHOWS', 'DUNGHEAPS', 'DUSTCOATS', 'DYSPRAXIC', 'EASTABOUT', 'EASTLANDS', 'ECHIURANS', 'ECHOGRAPH', 'ECOLODGES', 'ECOTARIAN',
    'ECPHRASES', 'ECPHRASIS', 'EGRESSIVE', 'EMAILINGS', 'ENANTHEMA', 'ENARGITES', 'ENNEAGRAM', 'ENQUEUING', 'EPICORMIC', 'EPIMERISE', 'EPIMERIZE', 'EQUIFINAL',
    'ESCABECHE', 'EUPHRASIA', 'EUTHANASE', 'EUTHANAZE', 'EXTRUSILE', 'FACEBOOKS', 'FACIALIST', 'FALLALISH', 'FARFALLES', 'FAULTLINE', 'FEIJOADAS', 'FEMICIDAL',
    'FEMICIDES', 'FILAGGRIN', 'FLATSTICK', 'FLECKIEST', 'FLIPPIEST', 'FLIPSIDES', 'FLYPOSTER', 'FLYSPRAYS', 'FOOTBRAKE', 'FOOTPUMPS', 'FORECADDY', 'FOURPLAYS',
    'FREECYCLE', 'FREEDIVER', 'FREERIDES', 'FUCKHEADS', 'FUGGINESS', 'FUSSBALLS', 'FUZZBOXES', 'GAMEYNESS', 'GASTROPUB', 'GENOTOXIC', 'GLAMMIEST', 'GLAMPINGS',
    'GLUEBALLS', 'GLYCATION', 'GNASHINGS', 'GNATWRENS', 'GOALWARDS', 'GOLDWORKS', 'GOODFELLA', 'GOOPINESS', 'GRAPELICE', 'GRAPHENES', 'GRASSBIRD', 'GREENEYES',
    'GRENACHES', 'GREYSCALE', 'GRITTINGS', 'GROUPWORK', 'GUESTBOOK', 'GUNSIGHTS', 'GUTLESSLY', 'GUYLINERS', 'HAEREMAIS', 'HANDKNITS', 'HARDTAILS', 'HEADWALLS',
    'HEARTSINK', 'HEATWAVES', 'HELICASES', 'HEXAPODAL', 'HIERATICS', 'HINAHINAS', 'HINDCASTS', 'HONOUREES', 'HOROKAKAS', 'HOTELINGS', 'HOTELLING', 'HYPERICIN',
    'IDEOPOLIS', 'ILLAWARRA', 'IMAGINEER', 'IMPOSEXES', 'INFOTECHS', 'INGRAINER', 'INSOURCED', 'INSOURCES', 'INTEGRINS', 'INTERWEBS', 'IRUKANDJI', 'ISOPTERAN',
    'JAILBAITS', 'JASMONATE', 'JATROPHAS', 'JINKERING', 'JOINTINGS', 'JOLIOTIUM', 'KAKARIKIS', 'KALOOKIES', 'KAMOKAMOS', 'KAREAREAS', 'KAZACHOCS', 'KENNELMAN',
    'KENNELMEN', 'KEYWORKER', 'KICKFLIPS', 'KILOPONDS', 'KILOTONNE', 'KINTLEDGE', 'KITEBOARD', 'KNARLIEST', 'KOHEKOHES', 'KORIMAKOS', 'KOROMIKOS', 'KRUMPINGS',
    'KUMIKUMIS', 'KUNEKUNES', 'LABELMATE', 'LACRIMARY', 'LACTIVISM', 'LACTIVIST', 'LAMPBRUSH', 'LANDMINED', 'LANDMINES', 'LAVANDINS', 'LAWCOURTS', 'LEETSPEAK',
    'LEUCISTIC', 'LIFEHACKS', 'LINKSPANS', 'LIONHEADS', 'LIPSALVES', 'LITREAGES', 'LONGLISTS', 'LONGWORMS', 'LOUNGIEST', 'LUVVIEDOM', 'LYCAENIDS', 'MACHINIMA',
    'MACROLIDE', 'MALLCORES', 'MARKETISE', 'MARKETIZE', 'MASSTIGES', 'MATFELLON', 'MEDALPLAY', 'MELITTINS', 'MELOXICAM', 'METAFILES', 'METAVERSE', 'MICKERIES',
    'MICROBLOG', 'MIDLANDER', 'MILLHANDS', 'MIMIVIRUS', 'MINIMARTS', 'MIROMIROS', 'MOBCASTED', 'MODAFINIL', 'MOKOMOKOS', 'MONOSKIED', 'MONOTASKS', 'MOONCAKES',
    'MUCHACHAS', 'MUCKYMUCK', 'MUDHOPPER', 'MUFFETTEE', 'MULESINGS', 'MULLAHING', 'MULLERING', 'MULTITOOL', 'MUMBLIEST', 'MURRHINES', 'MYOSTATIN', 'MYSPACING',
    'NALIDIXIC', 'NANOPORES', 'NANOWIRES', 'NARGUILEH', 'NOCHELING', 'NOROVIRUS', 'NOTCHELED', 'NOUGATINE', 'NOVEMBERS', 'NUNCHUCKS', 'OECOLOGIC', 'OFFSHORED',
    'ORLISTATS', 'OSSOBUCOS', 'OVERBANKS', 'OVERCLOCK', 'OVERCLUBS', 'OVERWRAPS', 'PACIFICAE', 'PACKCLOTH', 'PACKMULES', 'PAHAUTEAS', 'PANSTICKS', 'PARALOGUE',
    'PARAPARAS', 'PARGETTER', 'PAROTIDES', 'PARURESES', 'PARURESIS', 'PERIODISE', 'PERIODIZE', 'PERMALINK', 'PERMATANS', 'PETAFLOPS', 'PHOTOCARD', 'PHOTOSHOP',
    'PIDDLIEST', 'PIERHEADS', 'PIHOIHOIS', 'PINBOARDS', 'PINOTAGES', 'PLAYDOUGH', 'PLAYSLIPS', 'PLEURONIA', 'PLINKIEST', 'POLLAXING', 'POLYAMORY', 'POPSTRELS',
    'PORCHETTA', 'PORLOCKED', 'POUFFIEST', 'POUNDINGS', 'PREMISSED', 'PROCYONID', 'PRONKINGS', 'PROPENALS', 'PROSECCOS', 'PUNCHLINE', 'PUSHBIKES', 'QUADPLAYS',    
    'QUEENFISH', 'QUOININGS', 'RAZORCLAM', 'RAZORFISH', 'REALTONES', 'REBIRTHER', 'REBLOCHON', 'RECHIPPED', 'REDRESSAL', 'REGGAETON', 'REGIFTING', 'REPEREPES',
    'REPLICANT', 'REWATERED', 'REWILDING', 'RINGETTES', 'RITUXIMAB', 'ROANPIPES', 'ROMANESCO', 'ROOTBOUND', 'ROSETTING', 'ROTOSCOPE', 'SABREWING', 'SACRALITY',
    'SAMEYNESS', 'SARKINESS', 'SCALEABLE', 'SCALEABLY', 'SCENESTER', 'SCHELLIES', 'SCHMICKER', 'SCROBBLED', 'SCROBBLES', 'SCROLLERS', 'SCUZZBAGS', 'SEANNACHY',
    'SEMIWATER', 'SEROGROUP', 'SEROTYPIC', 'SHEDHANDS', 'SHITFACES', 'SHITHOUSE', 'SHMOOZERS', 'SHMOOZIER', 'SHOPWOMAN', 'SHOPWOMEN', 'SHORTARSE', 'SHOWJUMPS',
    'SHURIKENS', 'SILYMARIN', 'SKYRMIONS', 'SLANTIEST', 'SLAPPINGS', 'SLURPIEST', 'SMACKDOWN', 'SMELLABLE', 'SMOOCHIER', 'SNOWCLONE', 'SNOWDOMES', 'SNOWGLOBE',
    'SOURVELDS', 'SPARTICLE', 'SPLICINGS', 'SPLISHING', 'SPLITTISM', 'SPLITTIST', 'SPOOFIEST', 'SPOONHOOK', 'SPOONWORM', 'SQUITTERS', 'STACATION', 'STAGETTES',
    'STAGHORNS', 'STALAGMAS', 'STAPLINGS', 'STARGAZEY', 'STEEPLING', 'STEPOVERS', 'STINKBIRD', 'STOOZINGS', 'STORMCOCK', 'STRIMMING', 'STROKABLE', 'STUMPINGS',
    'SUBPRIMES', 'SUCKHOLES', 'SUNGAZERS', 'SUNGAZING', 'SUPERFOOD', 'SUPERTRAM', 'SUPREMUMS', 'SWANSONGS', 'SWATTIEST', 'SWEARIEST', 'SWEETLIPS', 'SWEETVELD',
    'SWINGARMS', 'SWINGBINS', 'SWINGTAIL', 'SYNTHASES', 'TALKTIMES', 'TANOREXIC', 'TEALIGHTS', 'TEHSILDAR', 'TELEWORKS', 'THIEFLIKE', 'THORNBIRD', 'THREEPEAT',
    'THROWDOWN', 'TIDELINES', 'TIGERWOOD', 'TIKTAALIK', 'TIMESHARE', 'TIMESTAMP', 'TINKERMAN', 'TINKERMEN', 'TONALITIC', 'TOOSHIEST', 'TOPSCORED', 'TOPSCORES',
    'TOXOCARAL', 'TRACKBEDS', 'TRANCIEST', 'TRANSCODE', 'TRAPFALLS', 'TREKKINGS', 'TRICKSILY', 'TRIGEMINI', 'TRITANOPE', 'TRUNKWORK', 'TURDUCKEN', 'UNCLIMBED',
    'UNCOMFIER', 'UNDELETES', 'UNFANCIED', 'UNFUNNIER', 'UPMARKETS', 'UPSELLING', 'VANTBRASS', 'VAWNTIEST', 'VILLIACOS', 'VLOGGINGS', 'VODCASTED', 'VODCASTER',
    'VOLUMISER', 'VOLUMIZER', 'WANTAWAYS', 'WEBIFYING', 'WEBISODES', 'WEIGHTAGE', 'WESTABOUT', 'WHINGIEST', 'WHITELIST', 'WHOLPHINS', 'WHUPPINGS', 'WIREFRAME',
    'XERAPHINS', 'ZANAMIVIR', 'ZIPLOCKED', 'ZOLPIDEMS', 'ZWANZIGER'
]

tenLetters = [
    'university', 'management', 'technology', 'government', 'department', 'categories', 'conditions', 'experience', 'activities', 'additional', 
    'washington', 'california', 'discussion', 'collection', 'conference', 'individual', 'everything', 'production', 'commercial', 'newsletter', 
    'registered', 'protection', 'employment', 'commission', 'electronic', 'particular', 'facilities', 'statistics', 'investment', 'industrial', 
    'associated', 'foundation', 'population', 'navigation', 'operations', 'understand', 'connection', 'properties', 'assessment', 'especially', 
    'considered', 'enterprise', 'processing', 'resolution', 'components', 'assistance', 'disclaimer', 'membership', 'background', 'trademarks', 
    'television', 'interested', 'throughout', 'associates', 'businesses', 'restaurant', 'procedures', 'themselves', 'evaluation', 'references', 
    'literature', 'respective', 'definition', 'networking', 'australian', 'guidelines', 'difference', 'directions', 'automotive', 'successful', 
    'publishing', 'developing', 'historical', 'scientific', 'functional', 'monitoring', 'dictionary', 'accounting', 'techniques', 'permission', 
    'generation', 'characters', 'apartments', 'designated', 'integrated', 'compliance', 'acceptance', 'strategies', 'affiliates', 'multimedia', 
    'leadership', 'comparison', 'determined', 'statements', 'completely', 'electrical', 'applicable', 'basketball', 'identified', 'frequently', 
    'laboratory', 'industries', 'expression', 'provisions', 'principles', 'compatible', 'consulting', 'recreation', 'parameters', 'introduced', 
    'originally', 'philosophy', 'regulation', 'prevention', 'healthcare', 'maintained', 'increasing', 'containing', 'guaranteed', 'convention', 
    'previously', 'conversion', 'reasonable', 'importance', 'javascript', 'objectives', 'structures', 'continuing', 'accordance', 'annotation', 
    'percentage', 'supporting', 'specialist', 'concerning', 'developers', 'equivalent', 'curriculum', 'psychology', 'appliances', 'elementary', 
    'controlled', 'authorized', 'retirement', 'efficiency', 'commitment', 'interviews', 'classified', 'confidence', 'consistent', 'securities', 
    'democratic', 'dimensions', 'contribute', 'challenges', 'submission', 'regulatory', 'inspection', 'manchester', 'continuous', 'initiative', 
    'disability', 'contractor', 'affordable', 'tournament', 'publishers', 'performing', 'absolutely', 'calculator', 'sufficient', 'resistance', 
    'candidates', 'biological', 'transition', 'instrument', 'favourites', 'relatively', 'represents', 'pittsburgh', 'revolution', 'mechanical', 
    'recognized', 'completion', 'milfhunter', 'accessible', 'birmingham', 'consultant', 'controller', 'committees', 'innovation', 'newspapers', 
    'programmes', 'eventually', 'agreements', 'innovative', 'conclusion', 'settlement', 'purchasing', 'instructor', 'bestiality', 'approaches', 
    'highlights', 'scientists', 'volunteers', 'attachment', 'calculated', 'appearance', 'parliament', 'situations', 'structural', 'prohibited', 
    'simulation', 'bankruptcy', 'substances', 'discovered', 'exhibition', 'nationwide', 'definitely', 'commentary', 'limousines', 'apparently', 
    'popularity', 'postposted', 'sacramento', 'impossible', 'depression', 'cincinnati', 'subsection', 'wallpapers', 'subsequent', 'motorcycle', 
    'disclosure', 'occupation', 'citysearch', 'atmosphere', 'experiment', 'federation', 'assignment', 'counseling', 'acceptable', 'medication', 
    'metabolism', 'personally', 'excellence', 'attributes', 'obligation', 'regardless', 'restricted', 'republican', 'attendance', 'adventures', 
    'appreciate', 'mechanisms', 'indicators', 'physicians', 'governance', 'capability', 'complaints', 'promotions', 'geographic', 'suspension', 
    'correction', 'supplement', 'admissions', 'convenient', 'displaying', 'encouraged', 'cartridges', 'automation', 'advantages', 'extensions', 
    'applicants', 'adjustment', 'treatments', 'camcorders', 'difficulty', 'collective', 'enrollment', 'interfaces', 'opposition', 'supervisor', 
    'attraction', 'customized', 'understood', 'amendments', 'attractive', 'recordings', 'polyphonic', 'adjustable', 'allocation', 'discipline', 
    'dispatched', 'installing', 'engagement', 'facilitate', 'subscriber', 'priorities', 'incredible', 'portuguese', 'everywhere', 'housewares', 
    'reputation', 'photograph', 'underlying', 'projection', 'diagnostic', 'automobile', 'downloaded', 'protective', 'sunglasses', 'preference', 
    'litigation', 'horizontal', 'ultimately', 'artificial', 'affiliated', 'activation', 'mitsubishi', 'processors', 'complexity', 'constantly', 
    'substitute', 'households', 'montgomery', 'louisville', 'algorithms', 'suggestion', 'connecting', 'proportion', 'essentials', 'protecting', 
    'separation', 'boundaries', 'luxembourg', 'deployment', 'colleagues', 'recruiting', 'prescribed', 'reproduced', 'queensland', 'addressing', 
    'discounted', 'bangladesh', 'constitute', 'graduation', 'variations', 'soundtrack', 'profession', 'separately', 'physiology', 'collecting', 
    'friendship', 'provincial', 'advertiser', 'encryption', 'possession', 'vegetables', 'thumbnails', 'respondent', 'accredited', 'compressed', 
    'scheduling', 'christians', 'impressive', 'relocation', 'violations', 'discretion', 'repository', 'generating', 'millennium', 'exceptions', 
    'macromedia', 'fellowship', 'copyrights', 'mastercard', 'chronicles', 'distribute', 'decorative', 'indigenous', 'validation', 'corruption', 
    'incentives', 'transcript', 'structured', 'reasonably', 'recommends', 'indicating', 'coordinate', 'limitation', 'widescreen', 'decorating', 
    'connectors', 'perception', 'infections', 'configured', 'analytical', 'assumption', 'technician', 'executives', 'supporters', 'withdrawal', 
    'veterinary', 'reflection', 'invitation', 'thumbzilla', 'translated', 'columnists', 'delivering', 'journalism', 'undertaken', 'identifier', 
    'conducting', 'impression', 'charleston', 'selections', 'projectors', 'vocational', 'pharmacies', 'completing', 'comparable', 'warranties', 
    'documented', 'paperbacks', 'vulnerable', 'transexual', 'mainstream', 'evaluating', 'volleyball', 'creativity', 'describing', 'quotations', 
    'behavioral', 'containers', 'screenshot', 'officially', 'consortium', 'recipients', 'traditions', 'humanities', 'britannica', 'visibility', 
    'strengthen', 'aggressive', 'determines', 'motivation', 'passengers', 'quantities', 'petersburg', 'powerpoint', 'obituaries', 'punishment', 
    'providence', 'remembered', 'wilderness', 'headphones', 'proceeding', 'volkswagen', 'subsidiary', 'terrorists', 'beneficial', 'threatened', 
    'prediction', 'ecological', 'consisting', 'submitting', 'mozambique', 'wellington', 'aboriginal', 'remarkable', 'preventing', 'productive', 
    'trackbacks', 'programmer', 'incomplete', 'legitimate', 'architects', 'unexpected', 'formatting', 'discussing', 'meaningful', 'blackberry', 
    'meditation', 'microphone', 'organizing', 'moderators', 'kazakhstan', 'kilometers', 'guarantees', 'indication', 'cigarettes', 'responding', 
    'physically', 'attempting', 'accurately', 'ministries', 'thoroughly', 'nottingham', 'identifies', 'interstate', 'systematic', 'madagascar', 
    'presenting', 'uzbekistan', 'richardson', 'fragrances', 'vocabulary', 'earthquake', 'geological', 'introduces', 'webmasters', 'acdbentity', 
    'conspiracy', 'cumulative', 'occasional', 'explicitly', 'girlfriend', 'influenced', 'complement', 'requesting', 'lauderdale', 'extraction', 
    'hypothesis', 'regression', 'collectors', 'recognised', 'azerbaijan', 'travelling', 'widespread', 'referenced', 'vietnamese', 'tremendous', 
    'surrounded', 'accomplish', 'vegetarian', 'ambassador', 'contacting', 'vegetation', 'infectious', 'continuity', 'phenomenon', 'charitable', 
    'burlington', 'researcher', 'qualifying', 'estimation', 'institutes', 'stationery', 'journalist', 'afterwards', 'signatures', 'simplified' 
]

elevenLetters = [
    'amenability', 'antecedence', 'attenuation', 'abracadabra', 'nachronism', 'adventuress', 'alternately', 'antechamber', 'ambiguously', 'assignation', 'adventurism', 'alternating',
    'aphrodisiac', 'alternation', 'adventurous', 'affirmation', 'lternative', 'attestation', 'affirmative', 'adverbially', 'acrimonious', 'acupressure', 'artlessness', 'amalgamated',
    'acupuncture', 'avoirdupois', 'apostleship', 'accumulator', 'rchipelago', 'aristocracy', 'ambitiously', 'anesthetize', 'acclamation', 'anticyclone', 'approaching', 'acclimation',
    'bureaucracy', 'befittingly', 'bereavement', 'bibliophile', 'eguilement', 'bivouacking', 'benediction', 'benedictory', 'benefaction', 'blessedness', 'bombardment', 'brittleness',
    'backsliding', 'botheration', 'beneficence', 'bimetallism', 'lamelessly', 'beneficiary', 'blameworthy', 'bicarbonate', 'boysenberry', 'barbarously', 'bedevilment', 'bicentenary',
    'brilliantly', 'burgomaster', 'brotherhood', 'breastplate', 'enevolence', 'bourgeoisie', 'brusqueness', 'bashfulness', 'bloodsucker', 'bifurcation', 'beastliness', 'biliousness',
    'comportment', 'connoisseur', 'colonialism', 'copperplate', 'lassically', 'confederacy', 'connotation', 'coagulation', 'correlation', 'cartography', 'countervail', 'ceremonious',
    'confederate', 'connotative', 'correlative', 'coruscation', 'onstricted', 'countermove', 'crepuscular', 'centreboard', 'calibration', 'constrictor', 'coordinator', 'culmination',
    'coincidence', 'criminology', 'centrepiece', 'chiropodist', 'ommunistic', 'consignment', 'catheterize', 'closefisted', 'composition', 'capillarity', 'celebration', 'cobblestone',
    'describable', 'directorate', 'degradation', 'delineation', 'evastating', 'devastation', 'detestation', 'destitution', 'delinquency', 'description', 'disapproval', 'discontinue',
    'descriptive', 'distraction', 'denominator', 'dissolutely', 'islocation', 'dissolution', 'disarmament', 'disparaging', 'destruction', 'desecration', 'development', 'disillusion',
    'destructive', 'divorcement', 'discordance', 'doctrinaire', 'istressful', 'differently', 'distressing', 'diplomatist', 'disciplined', 'deliverable', 'disposition', 'evangelical',
    'edification', 'endometrium', 'elicitation', 'equivocally', 'xpropriate', 'exclusively', 'enthralling', 'efficacious', 'egotistical', 'exasperated', 'externalize', 'equivocator',
    'eligibility', 'elucidation', 'efficiently', 'explainable', 'nlargement', 'explanation', 'elimination', 'explanatory', 'editorially', 'expurgation', 'eradication', 'embrocation',
    'earnestness', 'evaporation', 'excoriation', 'encapsulate', 'nlightened', 'embroiderer', 'exquisitely', 'expatiation', 'ejaculation', 'embroilment', 'engorgement', 'forgiveness',
    'floorwalker', 'fearfulness', 'formulation', 'fascinating', 'luoroscope', 'fascination', 'feasibility', 'familiarity', 'fomentation', 'familiarize', 'fluctuating', 'fornication',
    'fluctuation', 'flexibility', 'florescence', 'fulfillment', 'ashionable', 'frustrating', 'genteelness', 'geometrical', 'gallimaufry', 'graphically', 'gravitation', 'generically',
    'garnishment', 'homesteader', 'handicapped', 'harpsichord', 'ypertrophy', 'handicapper', 'hirsuteness', 'herpetology', 'hereinafter', 'hippocampus', 'humiliating', 'humiliation',
    'hemispheric', 'housewifely', 'hydrophobia', 'independent', 'njudicious', 'innumerable', 'inflammable', 'iconography', 'intentional', 'insincerely', 'impregnable', 'insincerity',
    'interviewer', 'joblessness', 'jackhammers', 'jackknifing', 'ardinieres', 'jacobinical', 'juvenescent', 'knucklehead', 'kindhearted', 'keyboardist', 'knowingness', 'kenogenesis',
    'kinetoscope', 'kilocalorie', 'kalashnikov', 'knuckleball', 'washiorkor', 'kinesiology', 'kleptocracy', 'ketosteroid', 'kitchenmaid', 'leatherneck', 'literalness', 'lucubration',
    'landholding', 'lingeringly', 'lubrication', 'lithography', 'egislating', 'legislation', 'legislative', 'logarithmic', 'leatherette', 'marginalize', 'meritorious', 'mockingbird',
    'monasticism', 'measureless', 'misconceive', 'measurement', 'etaphysics', 'musculature', 'malingering', 'matchmaking', 'monopolizer', 'mythologist', 'massiveness', 'mythologize',
    'misconstrue', 'nationality', 'nationalize', 'nonchalance', 'umerically', 'overflowing', 'obstetrical', 'orientating', 'orientation', 'operational', 'obliqueness', 'omnipotence',
    'opinionated', 'orthopedist', 'omnipresent', 'obstruction', 'mniscience', 'originality', 'overcareful', 'opportunism', 'opportunist', 'pterodactyl', 'patriarchal', 'portraitist',
    'pornography', 'prickliness', 'portraiture', 'purposeless', 'eritonitis', 'pamphleteer', 'personality', 'putrescence', 'personalize', 'progression', 'passiveness', 'presentment',
    'pretentious', 'quadrupling', 'quicksilver', 'quarrelsome', 'uizzically', 'quotability', 'querulously', 'quarantined', 'quarterback', 'quarterdeck', 'quintillion', 'quaveringly',
    'quislingism', 'quadraphony', 'quadrasonic', 'quadrennial', 'uiescently', 'quarterlies', 'quintuplets', 'questioners', 'quantifiers', 'quantifying', 'quarantines', 'referential',
    'reformation', 'reproachful', 'reformative', 'residential', 'eformatory', 'reluctantly', 'reminiscent', 'reclamation', 'rattlesnake', 'reduplicate', 'reiteration', 'reiterative',
    'requirement', 'requisition', 'resignation', 'receptivity', 'egretfully', 'repentantly', 'resourceful', 'reverberate', 'specialized', 'stroboscope', 'seventeenth', 'springiness',
    'splintering', 'suppuration', 'septicaemia', 'straightway', 'tockbroker', 'splayfooted', 'sponsorship', 'surrounding', 'spontaneity', 'sleepwalker', 'specifiable', 'spontaneous',
    'stockholder', 'sententious', 'solidifying', 'stethoscope', 'ubmergence', 'superficial', 'substantial', 'sentimental', 'suitability', 'shepherdess', 'synergistic', 'southwester',
    'transparent', 'trapezoidal', 'tempestuous', 'transporter', 'yrannicide', 'translation', 'theoretical', 'telegrapher', 'tobogganing', 'titillating', 'telegraphic', 'titillation',
    'turbulently', 'traditional', 'typewriting', 'territorial', 'hriftiness', 'translucent', 'unessential', 'unrighteous', 'uncivilized', 'unfurnished', 'unutterable', 'utilitarian',
    'unblemished', 'unconcerned', 'unfortunate', 'utilization', 'nderground', 'unorganized', 'undergrowth', 'underhanded', 'unrepentant', 'unflinching', 'uprightness', 'unavoidable',
    'ultramarine', 'unbelieving', 'unthinkable', 'vaccinating', 'accination', 'violoncello', 'venturesome', 'viticulture', 'viscountess', 'vindication', 'vicariously', 'vermiculite',
    'vicissitude', 'vertiginous', 'whippletree', 'wheresoever', 'omanliness', 'washerwoman', 'wherewithal', 'winsomeness', 'workmanlike', 'workmanship', 'wintergreen', 'wonderfully',
    'wonderingly', 'worldliness', 'whiffletree', 'westernmost', 'heelbarrow', 'wastebasket', 'wrongheaded', 'wealthiness', 'willingness', 'woodcarving', 'witheringly', 'windbreaker',
    'worthlessly', 'windcheater', 'waggishness', 'watercolour', 'atercourse', 'xerographic', 'xylophonist', 'xanthophyll', 'xenogenesis', 'xeranthemum', 'xanthelasma', 'xenoglossia',
    'xenogenetic', 'xiphisterna', 'xiphopagous', 'xenoplastic', 'eriscaping', 'xanthomonad', 'xerographer', 'xerophagies', 'xerotripsis', 'xanthations', 'xanthophyls', 'xanthopsias',
    'xenobiotics', 'xenogeneses', 'xenophobias', 'xenophobies', 'erochasies', 'yachtswoman', 'youthquakes', 'yarboroughs', 'yuckinesses', 'yatteringly', 'yumminesses', 'yellowbacks',
    'yellowbarks', 'yellowbirds', 'yellowcakes', 'yellowheads', 'ellowwares', 'yellowweeds', 'yellowwoods', 'yellowworts', 'yersinioses', 'yersiniosis', 'yesterevens', 'yellowshins',
    'youdendrift', 'zooplankton', 'zestfulness', 'zygomorphic', 'oomorphism', 'zealousness', 'zinnwaldite', 'zoroastrian', 'zanthoxylum', 'zinciferous', 'zoophytical', 'zincography',
    'zinkiferous', 'zebrafishes', 'zygopleural', 'zeolitiform', 'oogonidium', 'zoografting', 'zygotically', 'zoomagnetic', 'zoometrical', 'zymogenesis', 'zymotechnic', 'zymotically',
    'zigzaggiest', 'zillionaire', 'zinckenites' 
]

twelveLetters = [
    'astrological', 'apprehension', 'apprehensive', 'accidentally', 'appendicitis', 'adhesiveness', 'anathematize', 'accumulation', 'amalgamation', 'accumulative', 'assimilating', 'antediluvian', 'assimilation', 'announcement', 'astronomical', 'aristocratic', 'anatomically', 'administrate', 'approachable', 'alliteration', 'alliterative', 'abstractedly', 'anticipation', 'attitudinize', 'anticipatory', 'architecture', 'abstractness', 'advisability', 'augmentation', 'augmentative', 'agricultural', 'appropriator', 'abstruseness', 'arithmetical', 'allusiveness', 'alphabetical', 'bureaucratic', 'bacchanalian', 'beleaguering', 'benefactress', 'bullfighting', 'bachelorhood', 'beneficially', 'biographical', 'boisterously', 'bicentennial', 'bloodletting', 'brackishness', 'blandishment', 'bilingualism', 'bloodthirsty',    
    'breathlessly', 'backwoodsman', 'bluestocking', 'belletristic', 'bushwhacking', 'bactericidal', 'bewilderment', 'belligerence', 'belligerency', 'businesslike', 'bacteriology', 'bibliography', 'billingsgate', 'brontosaurus', 'biochemistry', 'beseechingly', 'bodybuilding', 'behaviourism', 'behaviourist', 'breakthrough', 'ceremonially', 'constraining', 'cartographer', 'condensation', 'contumacious', 'compensation', 'cancellation', 'cartographic', 'coordinately', 'contemporary', 'constricting', 'coordinating', 'constriction', 'coordination', 'contumelious', 'constrictive', 'childbearing', 'convincingly', 'coincidental', 'classifiable', 'contemptible', 'contemptibly', 'commercially', 'contemptuous', 'conviviality', 'colonization', 'childishness', 'construction', 'closemouthed', 'conciliation', 'constructive',    
    'consistently', 'conciliatory', 'counterclaim', 'chairmanship', 'disorienting', 'directorship', 'distractedly', 'divisibility', 'dissociation', 'denomination', 'dissociative', 'dethronement', 'disapproving', 'deliquescent', 'didactically', 'disfranchise', 'destructible', 'differential', 'discipleship', 'disciplinary', 'dissatisfied', 'denouncement', 'decipherable', 'distribution', 'dispossessed', 'distributive', 'dogmatically', 'disassociate', 'depopulation', 'disgorgement', 'diamagnetism', 'disinfectant', 'discouraging', 'disinfection', 'departmental', 'dispensation', 'doubtfulness', 'discourteous', 'disingenuous', 'disenchanted', 'embryologist', 'equalization', 'endangerment', 'entrancement', 'effervescent', 'effervescing', 'eavesdropper', 'encyclopedia', 'encyclopedic', 'embezzlement', 'equivocation',    
    'exasperating', 'estrangement', 'evangelistic', 'exasperation', 'enthronement', 'entreatingly', 'evisceration', 'embitterment', 'editorialize', 'enthusiastic', 'efflorescent', 'entanglement', 'entrepreneur', 'eleemosynary', 'extinguisher', 'expatriation', 'electrolysis', 'evolutionary', 'evolutionist', 'electrolytic', 'explicitness', 'emotionalism', 'enfeeblement', 'exploitation', 'fermentation', 'forestalling', 'fictionalize', 'flagellation', 'frontispiece', 'functionally', 'frangibility', 'formaldehyde', 'fundamentals', 'frankincense', 'felicitation', 'fibrillation', 'freethinking', 'fenestration', 'friendliness', 'facilitation', 'fluorescence', 'fraudulently', 'flammability', 'fainthearted', 'freakishness', 'fluorocarbon', 'fearlessness', 'feverishness', 'familiarised', 'familiarized', 'frontbencher',    
    'fruitfulness', 'frontiersman', 'faultfinding', 'fictitiously', 'flawlessness', 'figuratively', 'foreordained', 'fastidiously', 'geologically', 'genealogical', 'generational', 'gladiatorial', 'genuflection', 'governmental', 'governorship', 'galvanometer', 'geographical', 'guardianship', 'graciousness', 'gratuitously', 'geriatrician', 'gynecologist', 'globetrotter', 'gobbledygook', 'gluttonously', 'glockenspiel', 'graphologist', 'gamesmanship', 'geophysicist', 'geopolitical', 'gregariously', 'generousness', 'geochemistry', 'greathearted', 'gratefulness', 'gruesomeness', 'gratifyingly', 'gracefulness', 'gasification', 'goldbricking', 'glycogenesis', 'geometrician', 'globularness', 'gallinaceous', 'housebreaker', 'hypochondria', 'historically', 'housekeeping', 'hemstitching', 'handkerchief', 'henceforward',    
    'hypocritical', 'hierarchical', 'housewarming', 'heliocentric', 'hydrodynamic', 'hieroglyphic', 'hagiographer', 'hesitatingly', 'haberdashery', 'humorousness', 'handsomeness', 'hippopotamus', 'horsemanship', 'horizontally', 'habitability', 'hermetically', 'humanitarian', 'heartrending', 'humanization', 'hypothetical', 'hydrotherapy', 'horticulture', 'heartwarming', 'headmistress', 'hypertension', 'hypertensive', 'highlighting', 'heterosexual', 'intermission', 'inconsolable', 'intervention', 'intrauterine', 'irritability', 'intensifying', 'intermittent', 'indirectness', 'incoherently', 'illuminating', 'iconoclastic', 'illumination', 'independence', 'ineradicable', 'inarticulate', 'indiscipline', 'inflammation', 'insurrection', 'inflammatory', 'imperfection', 'incontinence', 'impregnation', 'indiscretion',    
    'infrequently', 'invigorating', 'instillation', 'intracranial', 'infringement', 'interference', 'invigoration', 'inaudibility', 'irregularity', 'incommodious', 'inauguration', 'inconvenient', 'journalistic', 'jurisdiction', 'juvenescence', 'jeopardizing', 'judicatories', 'jitterbugged', 'jeopardising', 'jeffersonian', 'jesuitically', 'judgmentally', 'juvenileness', 'journalizing', 'jurisconsult', 'jurisdictive', 'jurisprudent', 'justificator', 'judicatorial', 'jettisonable', 'juvenilities', 'journalising', 'jeopardously', 'jackanapeses', 'japonaiserie', 'juristically', 'jocularities', 'justiciaries', 'jaggednesses', 'journalisers', 'jerrymanders', 'journalizers', 'journallings', 'journeyworks', 'jailbreakers', 'jailbreaking', 'jovialnesses', 'joyfulnesses', 'kaleidoscope', 'kindergarten', 'knightliness',
    'kleptomaniac', 'karyokinesis', 'karyokinetic', 'kinaesthesis', 'kakistocracy', 'katharometer', 'katzenjammer', 'keratoplasty', 'knucklebones', 'kinaesthesia', 'kinaesthetic', 'kainogenesis', 'ketoacidosis', 'kitchenettes', 'knuckleheads', 'katamorphism', 'keratectasia', 'keratodermia', 'keratogenous', 'keratoiritis', 'keraunograph', 'keyboardists', 'kinesiatrics', 'kirschwasser', 'klipspringer', 'keratohyalin', 'ketoaciduria', 'kaleidophone', 'kilometrical', 'keratinizing', 'kinesthetics', 'knowableness', 'kiplingesque', 'legalization', 'labyrinthine', 'lexicography', 'loquaciously', 'longitudinal', 'lithographer', 'lithographic', 'longshoreman', 'legitimately', 'legitimatize', 'localization', 'liquefaction', 'lasciviously', 'lighthearted', 'lonesomeness', 'lugubriously', 'lopsidedness', 'licentiously',
    'lukewarmness', 'laboursaving', 'lifelessness', 'legitimatise', 'localisation', 'languorously', 'laundrywoman', 'listlessness', 'luminescence', 'lusciousness', 'levorotatory', 'lymphography', 'labyrinthian', 'ladylikeness', 'lexicologist', 'liturgiology', 'lepidomelane', 'laudableness', 'multifarious', 'moralization', 'misrepresent', 'maintainable', 'misapprehend', 'mysteriously', 'meetinghouse', 'misinterpret', 'ministration', 'mademoiselle', 'maximization', 'metaphysical', 'manslaughter', 'monopolistic', 'metaphorical', 'mythological', 'multilateral', 'magnetically', 'malleability', 'moderateness', 'misplacement', 'merchandiser', 'mineralogist', 'mechanically', 'merchantable', 'marriageable', 'memorability', 'manipulation', 'monosyllabic', 'manipulative', 'mulligatawny', 'magnetometer', 'monosyllable',
    'metropolitan', 'mistreatment', 'monomaniacal', 'nonexistence', 'nonconductor', 'northwestern', 'nonsensitive', 'neurasthenia', 'notification', 'noncombatant', 'nonessential', 'noncommittal', 'negativeness', 'navigability', 'nonchalantly', 'nomenclature', 'nonresistant', 'neurological', 'naturalistic', 'northeastern', 'nasalization', 'novelization', 'nonagenarian', 'northernmost', 'neighborhood', 'nonfictional', 'nonalcoholic', 'nonabsorbent', 'nonalignment', 'neurasthenic', 'newspaperman', 'nonflammable', 'neuroscience', 'nonexplosive', 'narcissistic', 'nonflowering', 'neurosurgeon', 'neurosurgery', 'neurotically', 'ostentatious', 'obsolescence', 'orthographic', 'obligatorily', 'obstetrician', 'occupational', 'obstreperous', 'omnipresence', 'obliteration', 'overestimate', 'oceanography', 'overexertion',
    'overreaching', 'organization', 'octogenarian', 'overwhelming', 'officeholder', 'onomatopoeia', 'onomatopoeic', 'outmanoeuvre', 'obscurantism', 'obscurantist', 'overcautious', 'overpowering', 'oligarchical', 'obsequiously', 'ossification', 'occasionally', 'overachiever', 'outstretched', 'orthopaedics', 'orthopaedist', 'overemphasis', 'otherworldly', 'outlandishly', 'optimization', 'perverseness', 'pleasantness', 'persistently', 'presentation', 'pumpernickel', 'passionately', 'patriarchate', 'pornographic', 'protuberance', 'partisanship', 'paleontology', 'praiseworthy', 'petrifaction', 'principality', 'putrefaction', 'partitioning', 'putrefactive', 'premeditated', 'prevaricator', 'preponderant', 'presentiment', 'preponderate', 'prolongation', 'propitiation', 'prerequisite', 'propitiatory', 'preventative',
    'penitentiary', 'preservation', 'professional', 'preservative', 'phrenologist', 'preconceived', 'protestation', 'preposterous', 'processional', 'quarterstaff', 'quintessence', 'questionable', 'questionably', 'quantitative', 'quadrangular', 'quixotically', 'quadriplegia', 'quadriplegic', 'quantifiable', 'quantization', 'quadraphonic', 'quarterfinal', 'quinquennium', 'quantisation', 'quarterlight', 'quadriphonic', 'quattrocento', 'quarantining', 'quadrenniums', 'quadricepses', 'quadrillions', 'questionings', 'quantitation', 'quarterbacks', 'quarterdecks', 'quelquechose', 'quinquennial', 'quadriennial', 'qualificator', 'quadrinomial', 'questionless', 'quantitively', 'quadrivalent', 'quantivalent', 'quaquaversal', 'relationship', 'reinvigorate', 'rhythmically', 'resoluteness', 'repatriation', 'renunciation',
    'receivership', 'reminiscence', 'reenlistment', 'restaurateur', 'reconcilable', 'radiographer', 'reproduction', 'recuperative', 'reproductive', 'redistribute', 'repercussion', 'reticulation', 'regeneration', 'resurrection', 'racketeering', 'recalcitrant', 'retrenchment', 'repossession', 'resuscitator', 'respectively', 'recognizable', 'rejuvenation', 'recognizance', 'remonstrance', 'rhododendron', 'ratification', 'reassessment', 'refrigerator', 'rightfulness', 'reassignment', 'spermatozoon', 'satisfaction', 'staggeringly', 'scandalously', 'southeastern', 'satisfactory', 'statistician', 'straightness', 'sarsaparilla', 'satisfyingly', 'southernmost', 'sleepwalking', 'supervention', 'specifically', 'swashbuckler', 'slovenliness', 'slipperiness', 'southwestern', 'subcommittee', 'substantiate', 'surveillance',
    'shuffleboard', 'stenographer', 'successively', 'stenographic', 'superannuate', 'segmentation', 'subjectivity', 'semiprecious', 'sharpshooter', 'subscription', 'substituting', 'steeplechase', 'stereoscopic', 'substitution', 'sexagenarian', 'tercentenary', 'transgressor', 'testamentary', 'tractability', 'transcendent', 'triumphantly', 'transitional', 'translatable', 'triglyceride', 'terrifically', 'tradespeople', 'telegraphist', 'thanksgiving', 'transduction', 'translucence', 'translucency', 'thoroughbred', 'thoroughfare', 'tangentially', 'trigonometry', 'thoroughness', 'theosophical', 'transmigrate', 'transferable', 'transference', 'transmission', 'thermometric', 'therapeutics', 'tuberculosis', 'teleological', 'transmitting', 'transmogrify', 'thundercloud', 'typification', 'technicality', 'transmutable',
    'unreservedly', 'untimeliness', 'unquestioned', 'unlikelihood', 'unlikeliness', 'universalism', 'universalist', 'unparalleled', 'universality', 'universalize', 'unconsidered', 'unmistakable', 'unsuccessful', 'unprincipled', 'unacceptable', 'unauthorized', 'ungainliness', 'unscrupulous', 'uncharitable', 'undercurrent', 'unseasonable', 'unbelievable', 'unseasonably', 'uninterested', 'ungovernable', 'unaccustomed', 'unprofitable', 'unregenerate', 'unfrequented', 'unacquainted', 'unanswerable', 'untrammelled', 'unprejudiced', 'unreasonable', 'unemployable', 'unemployment', 'vilification', 'vitalization', 'venerability', 'vocalization', 'vaporization', 'vociferation', 'veterinarian', 'vainglorious', 'vituperation', 'vituperative', 'victoriously', 'vitalisation', 'voluptuously', 'virtuousness', 'varicoloured',
    'vibraphonist', 'verification', 'vaudevillian', 'vocalisation', 'vindictively', 'vocationally', 'vociferously', 'volumetrical', 'vaporisation', 'variableness', 'vivification', 'vesiculation', 'valetudinary', 'volcanically', 'vaticination', 'vanquishable', 'viscosimeter', 'vermiculated', 'valuableness', 'verticalness', 'vaporousness', 'whimsicality', 'weatherboard', 'wretchedness', 'weatherproof', 'wainscotting', 'watchfulness', 'welterweight', 'whippoorwill', 'weightlifter', 'warmongering', 'waterproofed', 'wholehearted', 'wrongfulness', 'wastefulness', 'whortleberry', 'weatherglass', 'wollastonite', 'warehouseman', 'womanishness', 'windlessness', 'weisenheimer', 'woolgatherer', 'walkingstick', 'withstanding', 'weatherstrip', 'whitewashing', 'woodcarvings', 'wheelwrights', 'wallpapering', 'weathercocks',
    'wisecracking', 'watercourses', 'weightlessly', 'wildernesses', 'workingwoman', 'workingwomen', 'xylophonists', 'xiphisternum', 'xanthochroic', 'xanthochroid', 'xanthomatous', 'xylobalsamum', 'xerodermatic', 'xeromorphous', 'xanthochroia', 'xanthopterin', 'xiphiplastra', 'xanthophylls', 'xenodochiums', 'xenoglossias', 'xenoglossies', 'xeranthemums', 'xerographers', 'xerographies', 'xerophytisms', 'xiphopaguses', 'xylographers', 'xylographies', 'xylographing', 'xiphisternal', 'xenoparasite', 'xenosauridae', 'xerophthalmy', 'xanthogenate', 'xenopeltidae', 'xiphosternum', 'xiphosuridae', 'xenophontean', 'xenophontian', 'xenophontine', 'xenophoridae', 'xenopterygii', 'yellowhammer', 'youthfulness', 'yellowthroat', 'youngberries', 'yieldingness', 'yeastinesses', 'yellownesses', 'yesternights', 'yoctoseconds',
    'yamoussoukro', 'yellowshanks', 'yorkshireism', 'yorkshireman', 'yearnfulness', 'younghearted', 'youthfullity', 'yachtmanship', 'yezdegerdian', 'yarovization', 'yaroslavskiy', 'yttrocrasite', 'yttrogummite', 'yablonovskiy', 'yokeableness', 'yugoslavians', 'yazdegerdian', 'yellowjacket', 'zygomorphous', 'zoologically', 'zoophytology', 'zincographer', 'zygapophysis', 'zygodactylic', 'zoochemistry', 'zoogeography', 'zoographical', 'zalambdodont', 'zantedeschia', 'zoopathology', 'zincographic', 'zoospermatic', 'zoosporangia', 'zygapophyses', 'zootechnical', 'zinjanthropi', 'zootomically', 'zooxanthella', 'zygomycetous', 'zygomorphism', 'zoomagnetism', 'zwitterionic', 'zymotechnics', 'zoomastigote', 'zillionaires', 'zoantharians', 'zoanthropies', 'zoograftings', 'zoographists', 'zoomorphisms', 'zanthoxylums',
    'zooplankters', 'zooplanktons', 'zootherapies', 'backwardness', 'cryptography', 'enthrallment', 'faithfulness', 'hairsplitter', 'insalubrious'
]
   
# Hangman pics for wrong guesses
emptyStart = """
        ____
            |
            |
            |        
            |
            |
        ____|____
           
"""
wrongGuess1 = """
        ____
       |    |
            |
            |        
            |
            |
        ____|____
           
"""
wrongGuess2 = """
        ____
       |    |
       o    |
            |        
            |
            |
        ____|____
           
"""
wrongGuess3 = """
        ____
       |    |
       o    |
       |    |        
            |
            |
        ____|____
           
"""
wrongGuess4 = """
        ____
       |    |
       o    |
      /|    |        
            |
            |
        ____|____
           
"""
wrongGuess5 = """
        ____
       |    |
       o    |
      /|\   |        
            |
            |
        ____|____
           
"""
wrongGuess6 = """
        ____
       |    |
       o    |
      /|\   |        
      /     |
            |
        ____|____
           
"""
wrongGuess7 = """
        ____
       |    |
       o    |
      /|\   |        
      / \   |
            |
        ____|____
           
"""

# List for hangman pics
hangmanPics = [emptyStart, wrongGuess1, wrongGuess2, wrongGuess3, 
               wrongGuess4, wrongGuess5, wrongGuess6, wrongGuess7
]
# List to choose which length of letters for random word
masterList = [threeLetters, fourLetters, fiveLetters, 
              sixLetters,sevenLetters, eightLetters, nineLetters,
              tenLetters, elevenLetters, twelveLetters
]
# Loop is increased by one for each wrong guess
loop = 0

#Main Game Loop
while True:
    # Get length of random word
    while True:
        try:
            lengthChoice = int(input())
            if lengthChoice < 3 or lengthChoice > 12:
                raise ValueError
            randomWord = random.choice(masterList[lengthChoice - 3])
            break
        except ValueError:
            print("Please enter a number between 3 && 12.")
    
    wordList = list(randomWord.lower())
    # Create blank list for guesses
    guessList = ['_'] * lengthChoice
    alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
                    'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r',
                    's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
    usedLetters = []
    # Where main game logic runs      
    while True:
        if loop == 7:
            print(hangmanPics[loop])
            print(f'You have run out of guesses. The word was {randomWord}.')
            break
        elif guessList == wordList:
            print("You have guessed the word. Congratulations!")
            break
                    
        print(hangmanPics[loop])
        print(*guessList)
        print('--------------------------------')
        print('Used letters: ' )
        print(*usedLetters)
        print('Please enter your guess: ')
        
        while True:
            # Block for checking letter isnt used, in the alphabet and not greater than 1 letter
            try:
                x = input()  
                if len(x) != 1:
                    raise ValueError
                elif x in usedLetters:
                    raise ValueError
                elif x not in alphabetList:
                    raise ValueError
                elif x != str(x):
                    raise ValueError
                
                usedLetters.append(x)
                break
            except ValueError:
                print('Please enter an unused letter from the alphabet.')
        
        if x not in wordList:
            print('Not in the word.')
            loop += 1
        # Iterates through wordList and checks if the letter is in the wordList, and inserts the letter into the guessList
        elif x in wordList:
            for i in range(len(wordList)):
                if x == wordList[i]:
                    del guessList[i]
                    guessList.insert(i, x)           
    
    break 
            
                
        
        
                
