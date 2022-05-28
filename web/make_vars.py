import os

env_vars = {
    "api_url": os.environ.get("GDO_API_URL"),
    "api_url2": os.environ.get("GDO_API_URL")
}

with open('vars.js', 'w+') as vars_file:

    lines = [f"{key}:\"{val}\"," for key,val in env_vars.items()]
    lines = '\n\t'.join(lines)
    lines = lines[0:-1]
    vars_text = "export default env_vars = {\n" + lines + "\n}"

    vars_file.write(vars_text)