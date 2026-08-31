import json
import os
from collections import Counter

# ==============================================================================
# DATA STRUCTURE:
# contacts = {
#     1: {"name": "Awais", "phone": "+923011939995", "email": "awais@gmail.com", "tags": {"Python", "AI"}, "notes": ["AI Engineer"]}
# }
# ==============================================================================

contacts = {
    1: {
        "name": "Awais Ramzan",
        "phone": "+923011939995",
        "email": "awais@gmail.com",
        "tags": {"Python", "AI", "ML"},
        "notes": ["AI Engineer", "Met at hackathon"]
    },
    2: {
        "name": "Ahmad Ali",
        "phone": "+923059839320",
        "email": "ahmad@gmail.com",
        "tags": {"Python", "Web"},
        "notes": ["Frontend Developer"]
    },
    3: {
        "name": "Ali Hassan",
        "phone": "+923001234567",
        "email": "ali@gmail.com",
        "tags": {"Python", "Django"},
        "notes": ["Backend Developer"]
    }
}


# ==============================================================================
# 1. CORE CRUD FUNCTIONS
# ==============================================================================

def add_contact(contacts, name, phone, email, tags=None, notes=None):
    """Adds a new contact with unique ID and duplicate phone check."""
    # Check for duplicate phone
    for cid, c in contacts.items():
        if c["phone"] == phone:
            return (False, f"Contact already exists with phone '{phone}' (ID: {cid})", None)

    new_id = max(contacts.keys(), default=0) + 1
    new_contact = {
        "name": name.strip(),
        "phone": phone.strip(),
        "email": email.strip(),
        "tags": set(tags) if tags else set(),
        "notes": list(notes) if notes else []
    }
    contacts[new_id] = new_contact
    return (True, f"Contact '{name}' added successfully with ID: {new_id}!", new_contact)


def search_contacts(contacts, query):
    """Searches contacts by exact or partial match on name, phone, or email."""
    q = query.strip().lower()
    matches = {
        cid: c for cid, c in contacts.items()
        if q in c["name"].lower() or q in c["phone"].lower() or q in c["email"].lower()
    }
    if matches:
        return (True, f"Found {len(matches)} match(es):", matches)
    return (False, "No matching contacts found.", {})


def update_contact(contacts, contact_id, name=None, phone=None, email=None, new_note=None):
    """Updates contact details by ID."""
    if contact_id not in contacts:
        return (False, f"Contact ID {contact_id} not found!")

    c = contacts[contact_id]
    if name:
        c["name"] = name.strip()
    if phone:
        c["phone"] = phone.strip()
    if email:
        c["email"] = email.strip()
    if new_note:
        c["notes"].append(new_note.strip())

    return (True, f"Contact ID {contact_id} updated successfully!")


def delete_contact(contacts, contact_id):
    """Deletes a contact by ID."""
    if contact_id in contacts:
        deleted = contacts.pop(contact_id)
        return (True, f"Deleted contact '{deleted['name']}' (ID: {contact_id})")
    return (False, f"Contact ID {contact_id} not found!")


# ==============================================================================
# 2. ADVANCED SEARCH (COMPREHENSIONS)
# ==============================================================================

def advanced_search(contacts, name=None, tag=None, keyword=None):
    """Multi-criteria search using dictionary comprehensions."""
    results = {
        cid: c for cid, c in contacts.items()
        if (
            (name is None or name.lower() in c["name"].lower())
            and
            (tag is None or any(tag.lower() == t.lower() for t in c["tags"]))
            and
            (keyword is None or (
                keyword.lower() in c["name"].lower() or
                keyword.lower() in c["email"].lower() or
                any(keyword.lower() in note.lower() for note in c["notes"])
            ))
        )
    }
    return results


# ==============================================================================
# 3. TAG MANAGEMENT (SET OPERATIONS)
# ==============================================================================

def add_tag(contacts, contact_id, tag_name):
    """Adds a tag to a contact using set.add()."""
    if contact_id not in contacts:
        return (False, f"Contact ID {contact_id} not found!")
    contacts[contact_id]["tags"].add(tag_name.strip())
    return (True, f"Tag '{tag_name}' added to contact ID {contact_id}.")


def remove_tag(contacts, contact_id, tag_name):
    """Removes a tag from a contact using set.discard()."""
    if contact_id not in contacts:
        return (False, f"Contact ID {contact_id} not found!")
    if tag_name not in contacts[contact_id]["tags"]:
        return (False, f"Tag '{tag_name}' not found on contact ID {contact_id}.")
    contacts[contact_id]["tags"].discard(tag_name)
    return (True, f"Tag '{tag_name}' removed from contact ID {contact_id}.")


def find_by_tag(contacts, tag_name):
    """Finds contacts that have a specific tag using set intersection / membership."""
    tag_clean = tag_name.strip().lower()
    matches = {
        cid: c for cid, c in contacts.items()
        if any(t.lower() == tag_clean for t in c["tags"])
    }
    return matches


# ==============================================================================
# 4. EXPORT & IMPORT (JSON PERSISTENCE WITH ERROR HANDLING)
# ==============================================================================

def save_to_json(contacts, filename="contacts.json"):
    """
    Saves contacts to JSON file.
    Converts Sets to Lists since JSON cannot serialize Sets directly.
    """
    try:
        # Convert set of tags to list for JSON serialization
        serializable_contacts = {
            str(cid): {
                "name": c["name"],
                "phone": c["phone"],
                "email": c["email"],
                "tags": list(c["tags"]),
                "notes": c["notes"]
            }
            for cid, c in contacts.items()
        }
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(serializable_contacts, f, indent=4)
        return (True, f"Saved {len(contacts)} contacts to '{filename}' successfully!")
    except Exception as e:
        return (False, f"Failed to save contacts: {str(e)}")


def load_from_json(filename="contacts.json"):
    """
    Loads contacts from JSON file with error handling.
    Converts loaded tag lists back into Sets and string keys to integer IDs.
    """
    if not os.path.exists(filename):
        return (False, f"File '{filename}' does not exist.", {})

    try:
        with open(filename, "r", encoding="utf-8") as f:
            raw_data = json.load(f)

        loaded_contacts = {}
        for cid_str, c in raw_data.items():
            loaded_contacts[int(cid_str)] = {
                "name": c.get("name", ""),
                "phone": c.get("phone", ""),
                "email": c.get("email", ""),
                "tags": set(c.get("tags", [])),
                "notes": list(c.get("notes", []))
            }
        return (True, f"Loaded {len(loaded_contacts)} contacts from '{filename}'!", loaded_contacts)
    except json.JSONDecodeError:
        return (False, f"Error: '{filename}' contains invalid JSON formatting.", {})
    except Exception as e:
        return (False, f"Unexpected error while loading: {str(e)}", {})


# ==============================================================================
# 5. STATISTICS
# ==============================================================================

def get_statistics(contacts):
    """Calculates total contacts, tag usage distribution, and top tags."""
    total = len(contacts)
    if total == 0:
        return {
            "total_contacts": 0,
            "total_unique_tags": 0,
            "most_used_tags": [],
            "tag_counts": {}
        }

    # Collect all tags across all contacts
    all_tags = []
    for c in contacts.values():
        all_tags.extend(list(c["tags"]))

    tag_counter = Counter(all_tags)
    return {
        "total_contacts": total,
        "total_unique_tags": len(tag_counter),
        "most_used_tags": tag_counter.most_common(3),
        "tag_counts": dict(tag_counter)
    }


# ==============================================================================
# 6. HELPER DISPLAY FUNCTION
# ==============================================================================

def display_contacts(contact_dict):
    """Formats and prints contact dictionaries cleanly."""
    if not contact_dict:
        print("\n  [No contacts to display]")
        return

    print("\n" + "=" * 70)
    for cid, c in contact_dict.items():
        tags_str = ", ".join(sorted(c["tags"])) if c["tags"] else "None"
        notes_str = " | ".join(c["notes"]) if c["notes"] else "None"
        print(f"  [ID: {cid}] {c['name']}")
        print(f"      Phone: {c['phone']}  |  Email: {c['email']}")
        print(f"      Tags:  [{tags_str}]")
        print(f"      Notes: {notes_str}")
        print("  " + "-" * 66)
    print("=" * 70)


# ==============================================================================
# 7. INTERACTIVE CLI MENU
# ==============================================================================

def main_menu():
    global contacts
    while True:
        print("""
╔══════════════════════════════════════════════════╗
║        CONTACT MANAGEMENT SYSTEM (CMS)           ║
╠══════════════════════════════════════════════════╣
║  1. View All Contacts                            ║
║  2. Add New Contact                              ║
║  3. Search Contacts (Simple)                     ║
║  4. Advanced Search (Comprehension)              ║
║  5. Update Contact Details                       ║
║  6. Delete Contact                               ║
║  7. Tag Management (Add/Remove/Find by Tag)      ║
║  8. View System Statistics                       ║
║  9. Save to JSON File                            ║
║ 10. Load from JSON File                          ║
║  0. Exit                                         ║
╚══════════════════════════════════════════════════╝""")
        
        choice = input("Enter your choice (0-10): ").strip()

        # 1. VIEW ALL
        if choice == "1":
            display_contacts(contacts)

        # 2. ADD CONTACT
        elif choice == "2":
            print("\n--- Add New Contact ---")
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            email = input("Email: ").strip()
            raw_tags = input("Tags (comma separated, e.g. Work, AI): ").strip()
            note = input("Initial note (optional): ").strip()

            tag_set = {t.strip() for t in raw_tags.split(",") if t.strip()} if raw_tags else set()
            note_list = [note] if note else []

            success, msg, _ = add_contact(contacts, name, phone, email, tag_set, note_list)
            print(f"\n=> {msg}")

        # 3. SIMPLE SEARCH
        elif choice == "3":
            q = input("\nEnter search query (name/phone/email): ").strip()
            success, msg, matches = search_contacts(contacts, q)
            print(f"\n=> {msg}")
            display_contacts(matches)

        # 4. ADVANCED SEARCH
        elif choice == "4":
            print("\n--- Advanced Search (Press Enter to skip any filter) ---")
            name_q = input("Filter by name: ").strip() or None
            tag_q = input("Filter by tag: ").strip() or None
            kw_q = input("Filter by keyword in notes/email: ").strip() or None

            results = advanced_search(contacts, name=name_q, tag=tag_q, keyword=kw_q)
            print(f"\n=> Found {len(results)} matching contact(s):")
            display_contacts(results)

        # 5. UPDATE CONTACT
        elif choice == "5":
            cid_str = input("\nEnter Contact ID to update: ").strip()
            if not cid_str.isdigit() or int(cid_str) not in contacts:
                print("=> Invalid Contact ID!")
                continue
            
            cid = int(cid_str)
            curr = contacts[cid]
            print(f"\nEditing: {curr['name']}")
            new_name = input(f"New name (Enter to keep '{curr['name']}'): ").strip() or None
            new_phone = input(f"New phone (Enter to keep '{curr['phone']}'): ").strip() or None
            new_email = input(f"New email (Enter to keep '{curr['email']}'): ").strip() or None
            new_note = input("Add a new note (Enter to skip): ").strip() or None

            success, msg = update_contact(contacts, cid, new_name, new_phone, new_email, new_note)
            print(f"\n=> {msg}")

        # 6. DELETE CONTACT
        elif choice == "6":
            cid_str = input("\nEnter Contact ID to delete: ").strip()
            if cid_str.isdigit():
                success, msg = delete_contact(contacts, int(cid_str))
                print(f"\n=> {msg}")
            else:
                print("=> Invalid ID format!")

        # 7. TAG MANAGEMENT
        elif choice == "7":
            print("\n--- Tag Management ---")
            print("1. Add Tag to Contact")
            print("2. Remove Tag from Contact")
            print("3. Find Contacts by Tag")
            tag_choice = input("Select (1-3): ").strip()

            if tag_choice in ["1", "2"]:
                cid_str = input("Enter Contact ID: ").strip()
                if cid_str.isdigit() and int(cid_str) in contacts:
                    cid = int(cid_str)
                    tag_name = input("Enter Tag Name: ").strip()
                    if tag_choice == "1":
                        success, msg = add_tag(contacts, cid, tag_name)
                    else:
                        success, msg = remove_tag(contacts, cid, tag_name)
                    print(f"=> {msg}")
                else:
                    print("=> Contact ID not found!")
            elif tag_choice == "3":
                tag_name = input("Enter Tag Name to find: ").strip()
                matches = find_by_tag(contacts, tag_name)
                print(f"=> Found {len(matches)} contact(s) with tag '{tag_name}':")
                display_contacts(matches)

        # 8. STATISTICS
        elif choice == "8":
            stats = get_statistics(contacts)
            print("\n" + "=" * 45)
            print("         SYSTEM STATISTICS")
            print("=" * 45)
            print(f"  Total Contacts:     {stats['total_contacts']}")
            print(f"  Unique Tags:        {stats['total_unique_tags']}")
            print("\n  Top 3 Most Used Tags:")
            for tag, count in stats['most_used_tags']:
                print(f"    - {tag}: {count} contact(s)")
            print("\n  Contacts per Tag:")
            for tag, count in stats['tag_counts'].items():
                print(f"    - {tag}: {count}")
            print("=" * 45)

        # 9. SAVE TO JSON
        elif choice == "9":
            fname = input("Enter filename (default: contacts.json): ").strip() or "contacts.json"
            success, msg = save_to_json(contacts, fname)
            print(f"\n=> {msg}")

        # 10. LOAD FROM JSON
        elif choice == "10":
            fname = input("Enter filename (default: contacts.json): ").strip() or "contacts.json"
            success, msg, loaded = load_from_json(fname)
            print(f"\n=> {msg}")
            if success:
                contacts = loaded

        # 0. EXIT
        elif choice == "0":
            print("\nThank you for using Contact Management System. Goodbye! 👋\n")
            break
        else:
            print("\n=> Invalid option. Please enter a number between 0 and 10.")


# ==============================================================================
# ENTRY POINT
# ==============================================================================
if __name__ == "__main__":
    main_menu()