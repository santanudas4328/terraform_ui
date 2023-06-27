# Open the file for reading
with open('main.tf.json', 'r') as f:
    # Read the contents of the file
    contents = f.read()

# Look for the specific strings and replace them with new strings
new_contents = contents.replace('"[$', '["$').replace('}]"', '}"]').replace('"[]"', '[]').replace('                    "ingress": {', '                    "ingress": [{')

text1 = '                        "self": "false"\n                    }'
text2 = '                        "cidr_blocks": ["${aws_subnet.intDemoSubnet01.cidr_block}"]\n                    }'
text3 = '                        "description": "test"\n                    }'
text4 = '                        "from_port": "22"\n                    }'
text5 = '                        "ipv6_cidr_blocks": []\n                    }'
text6 = '                        "prefix_list_ids": []\n                    }'
text7 = '                        "protocol": "tcp"\n                    }'
text8 = '                        "security_groups": []\n                    }'
text9 = '                        "to_port": "22"\n                    }'
text10 = '                        "from_port": "0"\n                    }'
text11 = '                        "to_port": "0"\n                    }'
text12 = '                        "protocol": "-1"\n                    }'
text13 = '            "azurerm": {\n                "region": "ap-south-1"'
text14 = '            "google": {\n                "project": "terraform"'
text15 = '\\\\'
text16 = '"{\\"created_by\\":\\"santanu.das4328@tigeranalytics.com\\",\\"created_for\\":\\"demo\\"}"'

replacement1 = '                        "self": "false"\n                    }]'
replacement2 = '                        "cidr_blocks": ["${aws_subnet.intDemoSubnet01.cidr_block}"]\n                    }]'
replacement3 = '                        "description": "test"\n                    }]'
replacement4 = '                        "from_port": "22"\n                    }]'
replacement5 = '                        "ipv6_cidr_blocks": []\n                    }]'
replacement6 = '                        "prefix_list_ids": []\n                    }]'
replacement7 = '                        "protocol": "tcp"\n                    }]'
replacement8 = '                        "security_groups": []\n                    }]'
replacement9 = '                        "to_port": "22"\n                    }]'
replacement10 = '                        "from_port": "0"\n                    }]'
replacement11 = '                        "to_port": "0"\n                    }]'
replacement12 = '                        "protocol": "-1"\n                    }]'
replacement13 = '            "azurerm": {\n                "features": {}'
replacement14 = '            "google": {\n                "project": "cogent-tract-376005"'
replacement15 = '\\'
replacement16 = '{"created_by":"santanu.das4328@tigeranalytics.com","created_for":"demo"}'



for i in range(1,17):
    # new_contents = new_contents.replace(text  + str(i), replacement + str(i))
    new_contents = new_contents.replace(eval(f"text{i}"), eval(f"replacement{i}"))

# Open the file for writing
with open('main.tf.json', 'w') as f:
    # Write the new contents to the file
    f.write(new_contents)
