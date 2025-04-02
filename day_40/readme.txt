# Contact Manager

A Python dictionary-based contact management system that allows users to store and manage contact information including name, date of birth, telephone number, email address, and physical address.

## Features

- **Add Contacts**: Create new contact entries with validation for email addresses, phone numbers, and dates
- **View Contacts**: Display detailed information for specific contacts
- **List All Contacts**: View a list of all stored contacts
- **Update Contacts**: Modify information for existing contacts
- **Delete Contacts**: Remove contacts from the system
- **Search Functionality**: Find contacts based on any field
- **Data Persistence**: Contacts are saved to a JSON file and loaded on startup
- **Input Validation**: Ensures email addresses, phone numbers, and dates are in valid formats

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Installation

1. Clone this repository or download the `contact_manager.py` file
2. Ensure you have Python 3.6+ installed

## Usage

Run the script from your terminal or command prompt:

```bash
python contact_manager.py
```

### Menu Options

The application provides the following options:

1. **Add new contact** - Create a new contact entry
2. **View contact** - Display details for a specific contact
3. **List all contacts** - Show all stored contacts
4. **Update contact** - Modify an existing contact's information
5. **Delete contact** - Remove a contact from the system
6. **Search contacts** - Find contacts by searching across all fields
0. **Exit** - Close the application

## Data Storage

Contacts are stored in a JSON file named `contacts.json` in the same directory as the script. The JSON structure looks like this:

```json
{
    "John Doe": {
        "date_of_birth": "1990-01-15",
        "telephone": "123-456-7890",
        "email": "john.doe@example.com",
        "address": "123 Main St, Anytown, USA"
    },
    "Jane Smith": {
        "date_of_birth": "1985-05-22",
        "telephone": "987-654-3210",
        "email": "jane.smith@example.com",
        "address": "456 Oak Ave, Somewhere, USA"
    }
}
```

## Data Validation

- **Email addresses** must follow standard format (username@domain.extension)
- **Phone numbers** must contain 7-15 digits (spaces, dashes, and parentheses are allowed)
- **Dates** are accepted in multiple formats (YYYY-MM-DD, DD/MM/YYYY, etc.) and converted to YYYY-MM-DD for storage

## Project Structure

```
contact-manager/
├── contact_manager.py      # Main application file
├── contacts.json           # Data storage file (created when first contact is saved)
└── README.md               # This documentation file
```

## Future Enhancements

- Add import/export functionality for CSV and vCard formats
- Implement contact grouping/categorization
- Add birthday reminders
- Create a graphical user interface
- Add multi-user support with authentication

## License

This project is available under the MIT License.

## Author

Created as part of the 100 Days of Python challenge.