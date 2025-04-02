#!/usr/bin/env python3
"""
Contact Manager - A simple dictionary-based contact management system.
"""
import os
import json
import datetime
import re
from datetime import datetime

class ContactManager:
    def __init__(self, save_file="contacts.json"):
        """Initialize the contact manager with an empty contacts dictionary or load existing data."""
        self.save_file = save_file
        self.contacts = {}
        self.load_contacts()
    
    def load_contacts(self):
        """Load contacts from the JSON file if it exists."""
        if os.path.exists(self.save_file):
            try:
                with open(self.save_file, 'r') as file:
                    self.contacts = json.load(file)
                print(f"Loaded {len(self.contacts)} contacts from {self.save_file}")
            except json.JSONDecodeError:
                print("Error decoding contacts file. Starting with empty contacts.")
                self.contacts = {}
        else:
            print("No existing contacts file found. Starting with empty contacts.")
    
    def save_contacts(self):
        """Save contacts to the JSON file."""
        with open(self.save_file, 'w') as file:
            json.dump(self.contacts, file, indent=4)
        print(f"Saved {len(self.contacts)} contacts to {self.save_file}")
    
    def validate_email(self, email):
        """Validate email format using regex."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    def validate_phone(self, phone):
        """Validate phone number format."""
        # Remove spaces, dashes, parentheses for checking
        cleaned = re.sub(r'[\s\-\(\)]', '', phone)
        # Check if it contains only digits and has a reasonable length
        return cleaned.isdigit() and 7 <= len(cleaned) <= 15
    
    def validate_date(self, date_str):
        """Validate and convert date string to standard format."""
        date_formats = [
            '%Y-%m-%d',  # 1990-01-15
            '%d/%m/%Y',  # 15/01/1990
            '%m/%d/%Y',  # 01/15/1990
            '%d-%m-%Y',  # 15-01-1990
            '%d %b %Y',  # 15 Jan 1990
            '%d %B %Y'   # 15 January 1990
        ]
        
        for fmt in date_formats:
            try:
                date_obj = datetime.strptime(date_str, fmt)
                # Return standardized format
                return date_obj.strftime('%Y-%m-%d')
            except ValueError:
                continue
        
        return None
    
    def add_contact(self):
        """Add a new contact with validation."""
        print("\n=== Add New Contact ===")
        
        # Get name (required)
        while True:
            name = input("Name: ").strip()
            if name:
                break
            print("Name is required.")
        
        # Check if contact already exists
        if name in self.contacts:
            overwrite = input(f"Contact '{name}' already exists. Overwrite? (y/n): ").lower()
            if overwrite != 'y':
                print("Operation cancelled.")
                return
        
        # Get date of birth (with validation)
        while True:
            dob = input("Date of Birth (YYYY-MM-DD or DD/MM/YYYY): ").strip()
            if not dob:  # Optional field
                dob = ""
                break
                
            validated_dob = self.validate_date(dob)
            if validated_dob:
                dob = validated_dob
                break
            print("Invalid date format. Please use YYYY-MM-DD or DD/MM/YYYY.")
        
        # Get phone (with validation)
        while True:
            phone = input("Telephone: ").strip()
            if not phone:  # Optional field
                phone = ""
                break
                
            if self.validate_phone(phone):
                break
            print("Invalid phone format. Please enter a valid phone number.")
        
        # Get email (with validation)
        while True:
            email = input("Email Address: ").strip()
            if not email:  # Optional field
                email = ""
                break
                
            if self.validate_email(email):
                break
            print("Invalid email format. Please enter a valid email address.")
        
        # Get address
        address = input("Address: ").strip()
        
        # Create contact dictionary
        self.contacts[name] = {
            "date_of_birth": dob,
            "telephone": phone,
            "email": email,
            "address": address
        }
        
        print(f"\nContact '{name}' added successfully!")
        self.save_contacts()
    
    def view_contact(self):
        """View details of a specific contact."""
        if not self.contacts:
            print("\nNo contacts found.")
            return
            
        print("\n=== View Contact ===")
        name = input("Enter the name of the contact to view: ").strip()
        
        contact = self.contacts.get(name)
        if contact:
            print("\n=== Contact Details ===")
            print(f"Name: {name}")
            print(f"Date of Birth: {contact['date_of_birth']}")
            print(f"Telephone: {contact['telephone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
        else:
            print(f"Contact '{name}' not found.")
    
    def list_contacts(self):
        """List all contacts."""
        if not self.contacts:
            print("\nNo contacts found.")
            return
            
        print("\n=== Contact List ===")
        for i, (name, _) in enumerate(sorted(self.contacts.items()), 1):
            print(f"{i}. {name}")
    
    def delete_contact(self):
        """Delete a contact."""
        if not self.contacts:
            print("\nNo contacts found.")
            return
            
        print("\n=== Delete Contact ===")
        name = input("Enter the name of the contact to delete: ").strip()
        
        if name in self.contacts:
            confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ").lower()
            if confirm == 'y':
                del self.contacts[name]
                print(f"Contact '{name}' deleted successfully!")
                self.save_contacts()
            else:
                print("Deletion cancelled.")
        else:
            print(f"Contact '{name}' not found.")
    
    def update_contact(self):
        """Update an existing contact."""
        if not self.contacts:
            print("\nNo contacts found.")
            return
            
        print("\n=== Update Contact ===")
        name = input("Enter the name of the contact to update: ").strip()
        
        if name in self.contacts:
            contact = self.contacts[name]
            print("\nEnter new details (leave blank to keep current value):")
            
            # Update date of birth
            current_dob = contact['date_of_birth']
            print(f"Current Date of Birth: {current_dob}")
            while True:
                new_dob = input("New Date of Birth: ").strip()
                if not new_dob:  # Keep current value
                    new_dob = current_dob
                    break
                    
                validated_dob = self.validate_date(new_dob)
                if validated_dob:
                    new_dob = validated_dob
                    break
                print("Invalid date format. Please use YYYY-MM-DD or DD/MM/YYYY.")
            
            # Update phone
            current_phone = contact['telephone']
            print(f"Current Telephone: {current_phone}")
            while True:
                new_phone = input("New Telephone: ").strip()
                if not new_phone:  # Keep current value
                    new_phone = current_phone
                    break
                    
                if self.validate_phone(new_phone):
                    break
                print("Invalid phone format. Please enter a valid phone number.")
            
            # Update email
            current_email = contact['email']
            print(f"Current Email: {current_email}")
            while True:
                new_email = input("New Email: ").strip()
                if not new_email:  # Keep current value
                    new_email = current_email
                    break
                    
                if self.validate_email(new_email):
                    break
                print("Invalid email format. Please enter a valid email address.")
            
            # Update address
            current_address = contact['address']
            print(f"Current Address: {current_address}")
            new_address = input("New Address: ").strip()
            if not new_address:  # Keep current value
                new_address = current_address
            
            # Update the contact
            self.contacts[name] = {
                "date_of_birth": new_dob,
                "telephone": new_phone,
                "email": new_email,
                "address": new_address
            }
            
            print(f"\nContact '{name}' updated successfully!")
            self.save_contacts()
        else:
            print(f"Contact '{name}' not found.")
    
    def search_contacts(self):
        """Search contacts by name or other fields."""
        if not self.contacts:
            print("\nNo contacts found.")
            return
            
        print("\n=== Search Contacts ===")
        query = input("Enter search term: ").strip().lower()
        
        if not query:
            print("No search term provided.")
            return
            
        results = []
        
        # Search by name
        for name, details in self.contacts.items():
            if query in name.lower():
                results.append((name, "Name match"))
                continue
                
            # Search in other fields
            for field, value in details.items():
                if query in value.lower():
                    results.append((name, f"{field.capitalize()} match"))
                    break
        
        if results:
            print(f"\nFound {len(results)} match(es):")
            for i, (name, match_type) in enumerate(results, 1):
                print(f"{i}. {name} ({match_type})")
        else:
            print("No matches found.")
    
    def run(self):
        """Run the contact manager application."""
        while True:
            print("\n=== Contact Manager ===")
            print("1. Add new contact")
            print("2. View contact")
            print("3. List all contacts")
            print("4. Update contact")
            print("5. Delete contact")
            print("6. Search contacts")
            print("0. Exit")
            
            choice = input("\nEnter your choice (0-6): ").strip()
            
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contact()
            elif choice == '3':
                self.list_contacts()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                self.search_contacts()
            elif choice == '0':
                print("\nThank you for using Contact Manager! Goodbye.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    manager = ContactManager()
    manager.run()