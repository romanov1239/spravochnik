
            
from view import menu, show_contacts, print_message, input_contact, input_return, delete_contact,show_contact
import model
from view import text
from view import console



def start():
    while True:
        choice = menu()
        match choice:
            case 1:
                model.open_file()
                print_message(text.open_successful)
            case 2:
                pass
            case 3:
                show_contacts(model.phone_book)
            case 4:
                new = input_contact(text.input_new_contact)
                model.add_contact(new)
                print_message(text.contact_saved(new.get('name')))
            case 5:
                word = input_return(text.search_word)
                result = model.search(word)
                show_contacts(result)
            case 6:
                word = input_return(text.search_word)
                result = model.search(word)
                show_contacts(result)
                index = input_return(text.input_index)
                new = input_contact(text.input_change_contact)
                model.change(int(index), new)
                old_name = model.phone_book[int(index)-1].get('name')
                print_message(text.contact_changed(new.get('name') if new.get('name') else old_name))

            case 7:
                pb = model.pokaz_PB()
                show_contact(pb, text.telKnigaPusta)
                if pb:
                    index = console.input_index(pb, text.chtoUdalyaem)
                    if model.confirm(model.confirm_delete(pb[index - 1].get('name'))):
                        model.print_message(text.delete_contact(model.remove_contact(index)))        
            case 8:
                break