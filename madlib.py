import re

def print_intro():
    """Show intro and instructions to user."""
    print('Let\'s play madlibs. I\'ll ask you to provide some words based on a prompt. When you\'ve given all your answers, I\'ll tell you a story.)


def get_template_text(template_filename):
    """Get the template text from file and return as string."""
    with open(template_filename, 'r') as infile:
        return(infile.read())


def parse_template_text(template_text):
    """Parse the template text. Return a list of user prompts and the template text with the prompts stripped out."""
    pattern = '/\{(.*?)\}/g'
    return re.findall(pattern, template_text)


def get_user_responses(prompts):
    """Go through the list of prompts and reqcord user's answers. Return the answers in a list."""
    responses = []
    for prompt in prompts:
        responses.append(input(prompt))
    return responses


def format_template_text(template_text, prompts):
    """Replace the text blanks with the user's responses. Return the string."""
    pass


def print_formatted_text(template_text):
    """Print out the final text."""
    pass


def run():
    """Enter script execution."""
    show_intro()
    filename = 'template.txt'
    template_text = get_template_text(filename)
    prompts, template_text = parse_template_text(template_text)
    responses = get_user_responses(prompts)
    template_text = format_template_text(template_text, prompts)
    print_formatted_text(template_text)


if __name__ == '__main__':
    run()
