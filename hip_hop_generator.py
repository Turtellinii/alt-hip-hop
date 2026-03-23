import random
import sys
import os

# Import character generator function
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from importlib import import_module

def get_personality():
    """Generate a personality profile using character_generator.py"""
    spec = import_module('character generator')
    excluded_types = ['ISFJ', 'ESFJ', 'ISTJ', 'ESTJ']

    # Keep generating until we get a valid personality type
    while True:
        profile = spec.generate_mbti_profile()
        # Remove the first character and space (gender indicator) and return the rest
        parts = profile.split(' ', 1)
        if len(parts) > 1:
            personality = parts[1]
        else:
            personality = profile

        # Check if the MBTI type is excluded
        mbti_type = personality.split()[0] if personality else ""
        if mbti_type not in excluded_types:
            return personality

# Album names and rapper names
albums_and_rappers = [
    ("To Pimp a Butterfly", "Kendrick Lamar"),
    ("Madvillainy", "Madvillain"),
    ("Good kid, m.a.a.d city", "Kendrick Lamar"),
    ("Illmatic", "Nas"),
    ("Enter the Wu-Tang", "Wu-Tang"),
    ("My Beautiful Dark Twisted Fantasy", "Kanye West"),
    ("The Money Store", "Death Grips"),
    ("The College Dropout", "Kanye West"),
    ("Atrocity Exhibition", "Danny Brown"),
    ("The Low End Theory", ""),
    ("MM.. FOOD", "MF DOOM"),
    ("Exmilitary", "Death Grips"),
    ("Endtroducing", "DJ Shadow"),
    ("Donuts", "J Dilla"),
    ("Aquemini", "Outkast"),
    ("Late Registration", "Kanye West"),
    ("Midnight Marauders", ""),
    ("Liquid Swords", "GZA"),
    ("Pinata", "Madlib"),
    ("The Infamous", "Mobb Deep"),
    ("ATLiens", "Outkast"),
    ("Ready to Die", "The Notorious B.I.G."),
    ("LP!", "JPEGMAFIA"),
    ("We Got it From Here; Thank You 4 Your Service", ""),
    ("Flower Boy", "Tyler the Creator"),
    ("Jenny Death", "Death Grips"),
    ("Black on Both Sides", "Mos Def"),
    ("The Miseducation of Lauryn Hill", "Lauryn Hill"),
    ("KIDS SEE GHOSTS", "KIDS SEE GHOSTS"),
    ("Faces", "Mac Miller"),
    ("Yeezus", "Kanye West"),
    ("Sometimes I Might Be Introvert", "Little Simz"),
    ("Bottomless Pit", "Death Grips"),
    ("Vaudeville Villain", "Victor Vaughn"),
    ("Some Rap Songs", "Earl Sweatshirt"),
    ("Scaring the Hoes", "Danny Brown"),
    ("Modal Soul", "Nujabes"),
    ("The Forever Story", "JID"),
    ("Moment of Truth", "Gang Starr"),
    ("Things Fall Apart", "The Roots"),
    ("The Life of Pablo", "Kanye West"),
    ("By the Time I Get to Phoenix", "Injury Reserve"),
    ("Paul's Boutique", ""),
    ("It Takes a Nation of Millions to Hold Us Back", "Public Enemy"),
    ("Mista Thug Isolation", "Lil Ugly Mane"),
    ("Mystic Stylez", "Three-6 Mafia"),
    ("Cheat Codes", "Danger Mouse"),
    ("Stankonia", "Outkast"),
    ("Crack Cloud$ OVer Arts Kitchen", "Black Kray"),
    ("Only Built 4 Cuban Linx", "Raekwon"),
    ("Aethiopes", "billy woods"),
    ("Stress: The Extinction Agenda", "Organized Konfusion"),
    ("The Gospel According To", "Mach-Hommy"),
    ("Rodeo", "Travis Scott"),
    ("Deltron 3030", "Deltron 3030"),
    ("Black Star", "Mos Def"),
    ("Operation: Doomsday", "MF DOOM"),
    ("Be", "Common"),
    ("Lifestylez ov da Poor & Dangerous", "Big L"),
    ("XXX", "Danny Brown"),
    ("Veteran", "JPEGMAFIA"),
    ("All My Heroes Are Cornballs", "JPEGMAFIA"),
    ("DAYTONA", "Pusha T"),
    ("Reasonable Doubt", "Jay-Z"),
    ("Hell Hath No Fury", "Clipse"),
    ("6 Feet Deep", "Gravedigga"),
    ("The Blueprint", "Jay-Z"),
    ("Blowout Comb", "Digable Planets"),
    ("Bizarre Ride II", "The Pharcyde"),
    ("Buhloone Mindstate", "De La Soul"),
    ("Supreme Clientele", "Ghostface Killah"),
    ("Ridin Dirty", "UGK"),
    ("Maps", "billy woods"),
    ("Ironman", "Ghostface Killah"),
    ("Graduation", "Kanye West"),
    ("Gods Father", "Lil B"),
    ("Hiding Places", "billy woods"),
    ("The Cold Vein", "Cannibal Ox"),
    ("Call Me If You Get Lost", "Tyler the Creator"),
    ("Stakes Is High", "De La Soul"),
    ("Ser Humano!!", "Tiro de Gracia"),
    ("N*ggas on the Moon", "Death Grips"),
    ("Doggystyle", "Snoop Dogg"),
    ("Take Me to Your Leader", "King Geedorah"),
    ("Game Theory", ""),
    ("Run the Jewels 2", "Run the Jewels"),
    ("TABOO", "Denzel Curry"),
    ("Almighty So", "Chief Keef"),
    ("Bandana", "Freddie Gibbs"),
    ("The Chronic", "Dr. Dre"),
    ("Metaphorical Music", "Nujabes"),
    ("Melt My Eyez See Your Future", "Denzel Curry"),
    ("Visions of Bodies Being Burned", "clipping."),
    ("Veneno", "SpaceGhostPurrp"),
    ("Fear of a Black Planet", "Public Enemy"),
    ("3 Feet High and Rising", "De La Soul"),
    ("The Minstrel Show", "Little Brother"),
    ("GREY Area", "Little Simz"),
    ("Muerte", "Canserbero"),
    ("The Main Ingredient", "Pete Rock"),
    ("Illadelph Halflife", "The Roots"),
    ("Twerkin 10 Cellphone$", "Black Kray"),
    ("Mr. Morale & The Big Steppers", "Kendrick Lamar"),
    ("Labcabincalifornia", "The Pharcyde"),
    ("From Filthy Tongue of Gods and Griots", "Dalek"),
    ("The Black Album", "Jay-Z"),
    ("Manger on McNichols", "Boldy James"),
    ("Soul Food", "Goodie Mob"),
    ("Third Side of Tape", "Lil Ugly Mane"),
    ("People's Instinctive Travels and the Paths of Rhythm", ""),
    ("Saturation II", "BROCKHAMPTON"),
    ("Come - N - 2 - My World", "V.O.S."),
    ("4eva Is a Mighty Long Time", "Big K.R.I.T."),
    ("PART666%", "Yayayi"),
    ("Ill Communication", ""),
    ("Vicki Leekx", "VICKI LEEKX"),
    ("1999", "Joey Bada$$"),
    ("Art Brut", "PRO8L3M"),
    ("We Got It 4 Cheap Vol. 2", "Clipse"),
    ("Saturation III", "BROCKHAMPTON"),
    ("Dumpeister", "Mach-Hommy"),
    ("Mecca and the Soul Brother", "Pete Rock"),
    ("The Unseen", "Quasimoto"),
    ("Below the Heavens", "Blu"),
    ("Hell on Earth", "Mobb Deep"),
    ("History Will Absolve Me", "billy woods"),
    ("Die Lit", "Playboi Carti"),
    ("Da Devil's Playground: Underground Solo", "Koopsta Knicca"),
    ("The Diary", "Scarface"),
    ("A Day Late and a Dollar Short", ""),
    ("Monster", "Future"),
    ("Reachin", "Digable Planets"),
    ("Dreamcast Summer Songs", "The Rockwood Escape Plan"),
    ("Absence", "Dalek"),
    ("Goth Luv", "Black Kray"),
    ("Hard to Earn", "Gang Starr"),
    ("Ashes 2 Ashes, Dust 2 Dust", "Tommy Wright III"),
    ("A Piece of Strange", "CunninLynguist"),
    ("4, 5, 6", "Kool G Rap"),
    ("I Don't Like Shit I Don't Go Outside", "Earl Sweatshirt"),
    ("The Score", "Fugee"),
    ("Live and Let Die", "Kool G Rap"),
    ("93 Til' Infinity", "Souls of Mischief"),
    ("Super Tight", "UGK"),
    ("700 Dagreez", "Black Kray"),
    ("Haitian Body Odor", "Mach-Hommy"),
    ("Word…Life", "O.C."),
    ("Center of Attention", "Pete Rock"),
    ("Icedancer", "Bladee"),
    ("De La Soul Is Dead", "De La Soul"),
    ("Capital Punishment", "Big Pun"),
    ("Runnin-n-Gunnin", "Tommy Wright III"),
    ("Undun", ""),
    ("Scrapyard", "Quadeca"),
    ("Southernplayalisticadillacmuzik", "Outkast"),
    ("LiveLoveA$AP", "A$AP Rocky"),
    ("Bec", "Kunteynir"),
    ("Return to the 36 Chambers", "Ol' Dirty Bastard"),
    ("Fishscale", "Ghostface Killah"),
    ("Muddy Waters", "Redman"),
    ("Well Isn't This Awkward", "Charles Hamilton"),
    ("Alfredo", "The Alchemist"),
    ("Dare Iz a Darkside", "Redman"),
    ("The Devil's Playground", "Da Koopsta Knicca"),
    ("DAMN.", "Kendrick Lamar"),
    ("No Love Deep Web", "Death Grips"),
    ("Oblivion Access", "Lil Ugly Mane"),
    ("On Top of the World", "8Ball"),
    ("Death Certificate", "Ice Cube"),
    ("The Juggaknots", "Juggaknot"),
    ("Follow the Leader", "Rakim"),
    ("Like Water for Chocolate", "Common"),
    ("N*ggaz of Destruction", "N.O.D."),
    ("Beloved! Paradise! Jazz!?", "McKinley Dixon"),
    ("Fantastic Vol. 2", "Slum Village"),
    ("We Buy Diabetic Test Strips", "Armand Hammer"),
    ("It Was Written", "Nas"),
    ("Fantastic Damage", "El-P"),
    ("NO THANK YOU", "Little Simz"),
    ("The Don Killuminati: The 7 Day Theory", "Makaveli"),
    ("Me Against the World", "2Pac"),
    ("RTJ4", "Run the Jewels"),
    ("King's Disease III", "Nas"),
    ("Da Drought 3", "Lil Wayne"),
    ("Floss", "Injury Reserve"),
    ("Telefone", "Noname"),
    ("Vol. 9mm \"It's On\"", "Juicy J"),
    ("Aerolineas Makiza", "Makiza"),
    ("Dedication 2: Gangsta Grillz", "Lil Wayne"),
    ("Adromicfms 4", "Yung Beef"),
    ("Train of Thought", "Reflection Eternal"),
    ("Smoked Out Loced Out", "Three-6 Mafia"),
    ("Soundbombing II", "Rawkus"),
    ("The Sun Rises in the East", "Jeru the Damaja"),
    ("Part 3 Spring Mix '95", "Juicy J"),
    ("Babylon by Gus: Volume I", "Black Alien"),
    ("Resurrection", "Common Sense"),
    ("A Prince Among Thieves", "Prince Paul"),
    ("Swimming", "Mac Miller"),
    ("Pizza and Codeine", "Chris Travis"),
    ("King of da Playaz Ball", "Kingpin Skinny Pimp"),
    ("Dah Shinin'", "Smif-n-Wessun"),
    ("Reloaded", "Roc Marciano"),
    ("The Marshall Mathers LP", "Eminem"),
    ("There Existed an Addiction to Blood", "clipping."),
    ("Uptown Saturday Night", ""),
    ("On the Run", "Tommy Wright III"),
    ("The Lost Tapes", "Nas"),
    ("Back From the Dead 2", "Chief Keef"),
    ("Yayayi", "Yayayi"),
    ("Watch My Back", "LUCKI"),
    ("Volume 16: 4 Da Summer of '94", "Mista DJ Paul"),
    ("Labor Days", "Aesop Rock"),
    ("Funcrusher Plus", "Company Flow"),
    ("Mauvais Oeil", "Lunatic"),
    ("Brass", "Moor Mother"),
    ("Enta da Stage", "Black Moon"),
    ("GTBSG", ""),
    ("Breaking Atoms", "Main Source"),
    ("Castelos & Ruinas", "BK"),
    ("Romantizma", "Sagopa Kajmer"),
    ("Steal This Album", "The Coup"),
    ("Nocturnal", "Heltah Skeltah"),
    ("Dump Gawd: Hommy Edition", "Mach-Hommy"),
    ("Year of the Snitch", "Death Grips"),
    ("Burning Desire", "MIKE"),
    ("Paid In Full", "Rakim"),
    ("Organized Konfusion", "Organized Konfusion"),
    ("Daily Operation", "Gang Starr"),
    ("Luh Hertz", "Mach-Hommy"),
    ("Critical Beatdown", ""),
    ("Life After Death", "The Notorious B.I.G."),
    ("The Impossible Kid", "Aesop Rock"),
    ("4:44", "Jay-Z"),
    ("GUM", "Cities Aviv"),
    ("L'Ecole du Micro D'Argent", "IAM"),
    ("Quaranta", "Danny Brown"),
    ("Memento Mori", "Ovsyankin"),
    ("AmeriKKKa's Most Wanted", "Ice Cube"),
    ("AmeriKKKan Korruption", "Capital Steez"),
    ("Tana Talk 3", "Benny the Butcher"),
    ("Whut?", "Redman"),
    ("Internal Affairs", "Pharoahe Monch"),
    ("$vlena Gxmez Trvphov$$E Tvpe", "Black Kray")
]

# Extract unique rapper names (excluding empty ones)
rapper_names = list(set([name for _, name in albums_and_rappers if name]))
album_names = [album for album, _ in albums_and_rappers]

class Rapper:
    def __init__(self, name, personality, first_album_position):
        self.name = name
        self.personality = personality
        self.first_album_position = first_album_position
        self.region = random.choice(["East", "West", "South", "Midwest"])
        self.reserved_positions = []
        self.albums = []  # List of album positions this rapper appears in
        self.album_dates = {}  # Dictionary: position -> release_date string

class Group:
    def __init__(self, members, first_album_position):
        self.members = members  # List of Rapper objects
        self.first_album_position = first_album_position
        self.albums = []  # List of album positions

class Album:
    def __init__(self, position, name, primary_rapper, release_date, is_group, group_members=None, group=None):
        self.position = position
        self.name = name
        self.primary_rapper = primary_rapper
        self.release_date = release_date
        self.is_group = is_group
        self.group_members = group_members or []  # List of Rapper objects
        self.group = group  # Group object if reusing existing group

def determine_future_albums():
    """Determine how many future albums a rapper should have reserved"""
    roll = random.randint(1, 28)
    if 1 <= roll <= 7:
        return 0
    elif 8 <= roll <= 13:
        return 1
    elif 14 <= roll <= 18:
        return 2
    elif 19 <= roll <= 22:
        return 3
    elif 23 <= roll <= 25:
        return 4
    elif 26 <= roll <= 27:
        return 5
    else:  # 28
        return 6

def reserve_album_positions(rapper, current_position, already_reserved_set):
    """Reserve random positions from the remaining albums for this rapper"""
    num_reservations = determine_future_albums()
    print(f"      [DEBUG] Rapper {rapper.name} at #{current_position}: wants {num_reservations} reservations")
    print(f"      [DEBUG] Already reserved: {len(already_reserved_set)} positions")
    if num_reservations > 0 and current_position > num_reservations:
        # Only include positions that aren't already reserved
        available = [p for p in range(1, current_position) if p not in already_reserved_set]
        print(f"      [DEBUG] Available positions: {len(available)} out of {current_position-1}")
        if len(available) >= num_reservations:
            rapper.reserved_positions = random.sample(available, num_reservations)
            rapper.reserved_positions.sort(reverse=True)
            print(f"      [DEBUG] RESERVED: {rapper.reserved_positions}")
        else:
            print(f"      [DEBUG] Not enough available positions!")
    else:
        print(f"      [DEBUG] Cannot reserve (condition failed: {num_reservations} > 0 and {current_position} > {num_reservations})")

def generate_random_date(min_year=1985, max_year=2025):
    """Generate a random date between min_year and max_year"""
    # Ensure year range is valid
    min_year = max(1985, min_year)
    max_year = min(2025, max_year)
    if min_year > max_year:
        min_year, max_year = max_year, min_year

    year = random.randint(min_year, max_year)
    month = random.randint(1, 12)
    # Simple day generation (not accounting for month-specific days)
    day = random.randint(1, 28)
    return f"{month}/{day}/{year}"

def calculate_rapper_average_year(rapper):
    """Calculate the average release year for a rapper's existing albums"""
    if not rapper.album_dates:
        return None

    years = []
    for date_str in rapper.album_dates.values():
        # Parse date string "M/D/YYYY"
        parts = date_str.split('/')
        if len(parts) == 3:
            years.append(int(parts[2]))

    if years:
        return sum(years) // len(years)
    return None

def get_rapper_active_range(rapper, simulation_end=2025):
    """Return (lower, upper) year bounds for a rapper's next album.

    All of a rapper's albums must fall within a 14-year span.
    As their existing spread grows, the valid window narrows symmetrically:
      center = average of earliest and latest album years
      half_width = 14 - spread  (where spread = latest - earliest)
      range = [center - half_width, center + half_width]
    """
    if not rapper.album_dates:
        return None, None
    years = [int(d.split('/')[2]) for d in rapper.album_dates.values()]
    min_year = min(years)
    max_year = max(years)
    spread = max_year - min_year
    center = (min_year + max_year) / 2
    half_width = max(14 - spread, 0)
    lower = int(center - half_width)
    upper = min(int(center + half_width), simulation_end)
    return lower, upper

def find_rappers_within_timeframe(all_rappers_dict, current_date):
    """Find rappers whose active window includes the current date"""
    try:
        current_year = int(current_date.split('/')[2])

        valid_rapper_names = []
        for rapper_name, rapper in all_rappers_dict.items():
            if not rapper.album_dates:
                continue
            lower, upper = get_rapper_active_range(rapper)
            if lower <= current_year <= upper:
                valid_rapper_names.append(rapper_name)

        return valid_rapper_names
    except:
        return []

def generate_top_100():
    """Generate the top 100 albums"""
    print("\n" + "="*80)
    print("ALTERNATE HIP HOP HISTORY - TOP 100 ALBUMS")
    print("="*80 + "\n")

    albums = []
    all_rappers = {}  # Dictionary: rapper_name -> Rapper object
    all_groups = []  # List of Group objects
    reserved_positions = {}  # position -> Rapper object (for reservations)
    used_album_names = set()  # Track used album names to prevent duplicates

    num_group_albums = 0

    # Generate albums from position 100 down to 1
    for position in range(100, 0, -1):
        print(f"\n{'='*60}")
        print(f"POSITION #{position}")
        print(f"{'='*60}")

        # Check if ALL positions ahead are reserved (100% coverage)
        positions_ahead = set(range(1, position))
        reserved_ahead = set(reserved_positions.keys())
        unreserved_positions = positions_ahead - reserved_ahead

        all_reservations_filled = len(unreserved_positions) == 0

        print(f"[DEBUG] Positions ahead: {len(positions_ahead)}, Reserved: {len(reserved_ahead)}, Unreserved: {len(unreserved_positions)}")
        if len(unreserved_positions) > 0 and len(unreserved_positions) <= 20:
            print(f"[DEBUG] Unreserved positions: {sorted(unreserved_positions)}")
        print(f"[DEBUG] All reservations filled: {all_reservations_filled}")

        # Check if this position is reserved for a specific rapper
        if position in reserved_positions:
            primary_rapper = reserved_positions[position]
            # Generate release date within the rapper's current active window
            lower, upper = get_rapper_active_range(primary_rapper)
            if lower is not None:
                release_date = generate_random_date(lower, upper)
            else:
                release_date = generate_random_date()
        else:
            primary_rapper = None
            # Generate release date FIRST so we can filter group members by time
            release_date = generate_random_date()
        # Determine if this is a group album (33% chance) - applies to all positions
        is_group = random.random() < 0.33
        print(f"   [DEBUG] Position #{position}: is_group = {is_group}")

        # Select album name (ensure it hasn't been used before)
        available_album_names = [name for name in album_names if name not in used_album_names]
        if available_album_names:
            album_name = random.choice(available_album_names)
            used_album_names.add(album_name)
        else:
            # Fallback if we somehow run out (shouldn't happen with 274 names for 100 albums)
            album_name = random.choice(album_names)

        if position in reserved_positions and not is_group:
            # This is a reserved solo album
            primary_rapper.albums.append(position)
            primary_rapper.album_dates[position] = release_date

            # Remove this position from reserved_positions since we've processed it
            del reserved_positions[position]

            album = Album(
                position=position,
                name=album_name,
                primary_rapper=primary_rapper,
                release_date=release_date,
                is_group=False
            )
        elif is_group:
            num_group_albums += 1

            if primary_rapper is not None:
                # Primary rapper was reserved for this position - use them as group leader
                del reserved_positions[position]
            else:
                # Generate or select primary rapper
                release_year = int(release_date.split('/')[2])
                if all_reservations_filled and len(all_rappers) > 0:
                    # Can only use existing rappers - filter by active window
                    active_rappers = find_rappers_within_timeframe(all_rappers, release_date)
                    if active_rappers:
                        rapper_name = random.choice(active_rappers)
                    else:
                        rapper_name = random.choice(list(all_rappers.keys()))
                    primary_rapper = all_rappers[rapper_name]
                else:
                    rapper_name = random.choice(rapper_names)
                    if rapper_name in all_rappers:
                        existing = all_rappers[rapper_name]
                        lower, upper = get_rapper_active_range(existing)
                        if lower is None or lower <= release_year <= upper:
                            primary_rapper = existing
                        # else: primary_rapper stays None - existing rapper out of active window
                    if primary_rapper is None:
                        # Create a new rapper (name not found, or existing was out of active window)
                        if rapper_name in all_rappers:
                            unused = [n for n in rapper_names if n not in all_rappers]
                            rapper_name = random.choice(unused) if unused else random.choice(rapper_names)
                        personality = get_personality()
                        primary_rapper = Rapper(rapper_name, personality, position)
                        all_rappers[rapper_name] = primary_rapper
                        reserve_album_positions(primary_rapper, position, set(reserved_positions.keys()))
                        # Add all reservations to the dict
                        print(f"      [DEBUG] Adding {len(primary_rapper.reserved_positions)} reservations to dict")
                        for res_pos in primary_rapper.reserved_positions:
                            reserved_positions[res_pos] = primary_rapper
                        print(f"      [DEBUG] Dict now has {len(reserved_positions)} total reservations")

            primary_rapper.albums.append(position)
            primary_rapper.album_dates[position] = release_date

            # Check if primary rapper has been in any groups before
            rapper_groups = [group for group in all_groups if primary_rapper in group.members]
            print(f"   [DEBUG] Position #{position}: {primary_rapper.name} has been in {len(rapper_groups)} group(s) before")

            # 50% chance to reuse existing group if they've been in groups before
            if rapper_groups and random.random() < 0.5:
                print(f"   [DEBUG] Position #{position}: using former group (reusing existing group)")
                # If they've been in multiple groups, randomly select one
                existing_group = random.choice(rapper_groups)
                group_members = existing_group.members
                existing_group.albums.append(position)
                # Track this album date for all group members
                for member in group_members:
                    if position not in member.albums:
                        member.albums.append(position)
                    member.album_dates[position] = release_date
                album = Album(
                    position=position,
                    name=album_name,
                    primary_rapper=primary_rapper,
                    release_date=release_date,
                    is_group=True,
                    group_members=group_members,
                    group=existing_group
                )
            else:
                # Create new group
                print(f"   [DEBUG] Position #{position}: creating new group")
                num_members = random.randint(2, 5)
                group_members = [primary_rapper]

                # Generate other members
                for _ in range(num_members - 1):
                    if all_reservations_filled:
                        # Can only use existing rappers - filter by active window
                        if len(all_rappers) > 1:
                            # Find rappers still within their 20-year active window
                            valid_rappers = find_rappers_within_timeframe(all_rappers, release_date)
                            # Exclude rappers already in this group
                            available_rappers = [name for name in valid_rappers if all_rappers[name] not in group_members]

                            if available_rappers:
                                member_name = random.choice(available_rappers)
                                member = all_rappers[member_name]
                            else:
                                # If no rappers in timeframe, just pick any existing rapper not in group
                                available_rappers = [name for name in all_rappers.keys() if all_rappers[name] not in group_members]
                                if available_rappers:
                                    member_name = random.choice(available_rappers)
                                    member = all_rappers[member_name]
                                else:
                                    # If no available rappers, skip this member
                                    continue
                        else:
                            # Not enough existing rappers, skip this member
                            continue
                    else:
                        # 50% chance new rapper, 50% existing rapper
                        if random.random() < 0.5 and len(all_rappers) > 0:
                            # Find existing rappers still within their 20-year active window
                            valid_rappers = find_rappers_within_timeframe(all_rappers, release_date)
                            # Exclude rappers already in this group
                            valid_rappers = [name for name in valid_rappers if all_rappers[name] not in group_members]

                            if valid_rappers:
                                member_name = random.choice(valid_rappers)
                                member = all_rappers[member_name]
                            else:
                                # No valid rappers in timeframe, create new one
                                member_name = random.choice(rapper_names)
                                while member_name in [m.name for m in group_members]:
                                    member_name = random.choice(rapper_names)

                                if member_name in all_rappers:
                                    member = all_rappers[member_name]
                                else:
                                    personality = get_personality()
                                    member = Rapper(member_name, personality, position)
                                    all_rappers[member_name] = member
                                    reserve_album_positions(member, position, set(reserved_positions.keys()))
                                    # Add all reservations to the dict
                                    print(f"      [DEBUG] Adding {len(member.reserved_positions)} reservations to dict")
                                    for res_pos in member.reserved_positions:
                                        reserved_positions[res_pos] = member
                                    print(f"      [DEBUG] Dict now has {len(reserved_positions)} total reservations")
                        else:
                            # New rapper
                            member_name = random.choice(rapper_names)
                            while member_name in [m.name for m in group_members]:
                                member_name = random.choice(rapper_names)

                            if member_name in all_rappers:
                                member = all_rappers[member_name]
                            else:
                                personality = get_personality()
                                member = Rapper(member_name, personality, position)
                                all_rappers[member_name] = member
                                reserve_album_positions(member, position, set(reserved_positions.keys()))
                                # Add all reservations to the dict
                                print(f"      [DEBUG] Adding {len(member.reserved_positions)} reservations to dict")
                                for res_pos in member.reserved_positions:
                                    reserved_positions[res_pos] = member
                                print(f"      [DEBUG] Dict now has {len(reserved_positions)} total reservations")

                    if member not in group_members:
                        group_members.append(member)
                        member.albums.append(position)
                        member.album_dates[position] = release_date

                new_group = Group(group_members, position)
                new_group.albums.append(position)
                all_groups.append(new_group)

                album = Album(
                    position=position,
                    name=album_name,
                    primary_rapper=primary_rapper,
                    release_date=release_date,
                    is_group=True,
                    group_members=group_members,
                    group=new_group
                )
        else:
            # Solo album
            release_year = int(release_date.split('/')[2])
            if all_reservations_filled and len(all_rappers) > 0:
                # Can only use existing rappers - filter by active window
                active_rappers = find_rappers_within_timeframe(all_rappers, release_date)
                if active_rappers:
                    rapper_name = random.choice(active_rappers)
                else:
                    rapper_name = random.choice(list(all_rappers.keys()))
                primary_rapper = all_rappers[rapper_name]
            else:
                rapper_name = random.choice(rapper_names)
                if rapper_name in all_rappers:
                    existing = all_rappers[rapper_name]
                    lower, upper = get_rapper_active_range(existing)
                    if lower is None or lower <= release_year <= upper:
                        primary_rapper = existing
                    # else: primary_rapper stays None - existing rapper out of active window
                if primary_rapper is None:
                    # Create a new rapper (name not found, or existing was out of active window)
                    if rapper_name in all_rappers:
                        unused = [n for n in rapper_names if n not in all_rappers]
                        rapper_name = random.choice(unused) if unused else random.choice(rapper_names)
                    personality = get_personality()
                    primary_rapper = Rapper(rapper_name, personality, position)
                    all_rappers[rapper_name] = primary_rapper
                    reserve_album_positions(primary_rapper, position, set(reserved_positions.keys()))
                    # Add all reservations to the dict
                    print(f"      [DEBUG] Adding {len(primary_rapper.reserved_positions)} reservations to dict")
                    for res_pos in primary_rapper.reserved_positions:
                        reserved_positions[res_pos] = primary_rapper
                    print(f"      [DEBUG] Dict now has {len(reserved_positions)} total reservations")

            primary_rapper.albums.append(position)
            primary_rapper.album_dates[position] = release_date

            album = Album(
                position=position,
                name=album_name,
                primary_rapper=primary_rapper,
                release_date=release_date,
                is_group=False
            )

        albums.append(album)

        # Print album in final format
        print(f"#{album.position} - {album.name}")
        if album.is_group:
            member_names = ", ".join([m.name for m in album.group_members])
            print(f"   Artists: {member_names}")
            for member in album.group_members:
                print(f"      - {member.name}: {member.personality}")
        else:
            print(f"   Artist: {album.primary_rapper.name}")
            print(f"      Personality: {album.primary_rapper.personality}")
        print(f"   Release Date: {album.release_date}")
        print()

    return albums

def print_top_100(albums):
    """Print the top 100 list"""
    print("\n" + "="*80)
    print("ALTERNATE HIP HOP HISTORY - TOP 100 ALBUMS")
    print("="*80 + "\n")

    for album in albums:
        print(f"#{album.position} - {album.name}")
        if album.is_group:
            member_names = ", ".join([m.name for m in album.group_members])
            print(f"   Artists: {member_names}")
            for member in album.group_members:
                print(f"      - {member.name}: {member.personality}")
        else:
            print(f"   Artist: {album.primary_rapper.name}")
            print(f"      Personality: {album.primary_rapper.personality}")
        print(f"   Release Date: {album.release_date}")
        print()

def print_chronological(albums):
    """Print albums in chronological order"""
    # Sort by release date
    import datetime

    def parse_date(date_str):
        month, day, year = map(int, date_str.split('/'))
        return datetime.datetime(year, month, day)

    sorted_albums = sorted(albums, key=lambda x: parse_date(x.release_date))

    print("\n" + "="*80)
    print("CHRONOLOGICAL ORDER")
    print("="*80 + "\n")

    for i, album in enumerate(sorted_albums, 1):
        if album.is_group:
            # Format: Rapper Name, Personality, Region;; Rapper Name, Personality, Region
            artists = ";; ".join([f"{m.name}, {m.personality}, {m.region}" for m in album.group_members])
            print(f"{i}. {album.name} ({artists}) [{album.release_date}] {{{album.position}}}")
        else:
            r = album.primary_rapper
            print(f"{i}. {album.name} ({r.name}, {r.personality}, {r.region}) [{album.release_date}] {{{album.position}}}")

def print_rapper_scores(albums):
    """Print rappers ranked by total points earned across all albums.

    Each album awards (100 - position) points, split equally among all
    rappers who worked on it.
    """
    scores = {}   # rapper_name -> total points (float)
    rappers = {}  # rapper_name -> Rapper object

    for album in albums:
        points = 100 - album.position
        workers = album.group_members if album.is_group else [album.primary_rapper]
        share = points / len(workers)
        for rapper in workers:
            scores[rapper.name] = scores.get(rapper.name, 0) + share
            rappers[rapper.name] = rapper

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    print("\n" + "="*80)
    print("RAPPER RANKINGS BY POINTS")
    print("="*80 + "\n")

    for i, (name, pts) in enumerate(ranked, 1):
        rapper = rappers[name]
        years = [int(d.split('/')[2]) for d in rapper.album_dates.values()]
        year_range = f"{min(years)}-{max(years)}" if years else "N/A"
        print(f"{i}. {name} - {pts:.1f} pts")
        print(f"   {rapper.personality} | {rapper.region} | {year_range}")

if __name__ == "__main__":
    random.seed()  # Use current time as seed for randomness
    albums = generate_top_100()
    print_chronological(albums)
    print_rapper_scores(albums)
