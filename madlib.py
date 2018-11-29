import re


def print_intro():
    """Show intro and instructions to user."""
    print('Let\'s play madlibs. I\'ll ask you to provide some words based on a prompt. When you\'ve given all your answers, I\'ll tell you a story.')


def get_template_text(template_filename):
    """Get the template text from file and return as string."""
    with open(template_filename, 'r') as infile:
        return(infile.read())


def parse_template_text(template_text):
    """Parse the template text. Return a list of user prompts and the template text with the prompts stripped out."""
    pattern = '\{(.*?)\}'
    prompts = re.findall(pattern, template_text)
    template_text = re.sub(pattern, '{}', template_text)
    return template_text, prompts


def get_user_responses(prompts):
    """Go through the list of prompts and reqcord user's answers. Return the answers in a list."""
    responses = []
    for prompt in prompts:
        responses.append(input(f'Enter a {prompt.lower()}: '))
    return responses


def format_template_text(template_text, responses):
    """Replace the text blanks with the user's responses. Return the string."""
    return template_text.format(*responses)


def print_formatted_text(template_text):
    """Print out the final text."""
    print(template_text)


def write_to_file(filename, template_text):
    """Open a file for writing and write the template_text into it."""
    with open(filename, 'w') as out_file:
        out_file.write(template_text)


def run():
    """Enter script execution."""
    print_intro()
    filename = 'template.txt'
    template_text = get_template_text(filename)
    template_text, prompts = parse_template_text(template_text)
    responses = get_user_responses(prompts)
    template_text = format_template_text(template_text, responses)
    print_formatted_text(template_text)
    out_filename = 'madlib.txt'
    write_to_file(out_filename, template_text)


if __name__ == '__main__':
    run()
