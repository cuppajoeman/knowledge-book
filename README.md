Everything is known as a structure:

# Structure
    * A top level content file called `content.tex`
    * definitions - a directory full of single files which contain a single definition
    * theorems - above for theorems
    * lemmas - above for lemmas
    * examples - above for examples
    * substructures - Other instances of structures (recursive)

Say we want to make a new geometry section, then all we have to do is do `cp structure geometry` and and start by filling out the content folder. 
Then if want to add a substructure to geometry I can do `cp structure geometry/substructures/triangles` (and note that it may have multiple sub-structures). So in general adding a structure at depth n looks like: (w.r.t the root directory) `cp structure struct_name_0/substructures/struct_name_1/substructures/.../struct_name_n/substructures/new_structure_name`.

