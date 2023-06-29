#!/bin/bash -x

output_dir_rules=/home/karima/datasets/rules

mkdir -p  ${output_dir_rules}
cd ${output_dir_rules}
git clone --depth 1 https://github.com/Yamato-Security/hayabusa-rules
git clone --depth 1 https://github.com/SigmaHQ/sigma

for file in $(find . -name '*.yml'); do
    [ -f "$file" ] || break
	yq ".rulePath = \"${file}\"" -o=json  $file > ${file}.json
done

cmemc graph delete http://example.com/rule

for file in $(find . -name '*.json'); do
    [ -f "$file" ] || break
    cmemc workflow io  RulesHayabusaSigma_671e1f43d94bbc36:Importrules_6ccbc14b656c75c9 -i ${file}
done