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

cmemc -c test graph delete http://example.com/rule

for file in $(find . -name '*.json'); do
    [ -f "$file" ] || break
    cmemc -c test workflow io  RulesHayabusaSigma_0acd314cabf95ef2:Importrules_a1e8e349bc9563c6 -i ${file}
done