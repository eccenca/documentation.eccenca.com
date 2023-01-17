### **Improve the linking rule.**

To improve the linking rule, need to add the release date information.

- Click on the **linking** editor then click on the **source path** and drag the release date on the canvas.

![image](source-releasedate.png)

- Click on the **target path** and drag the release date on the canvas.
![image](target-releasedate.png)

- Click on **transform** and type the date and drag the parse date pattern on the canvas twice.

![image](date-pattern.png)

- Drag the little dot on the right side of the source path box and target path box (release date) onto the left dot of the transformation box(parse date) to connect the two with a line (you always must drag from the right side of one element to the left side of another to connect the two).

![image](date-connects.png)

- Click on transform type date and drag on the canvas and type 365 in the threshold field (It allows the comparator computes the distance in days between two dates.

![image](date.png)

- Drag the little dot on the right side of both parse date patterns onto the left dot of the transformation box(date) to connect the two with a line (you always must drag from the right side of one element to the left side of another to connect the two). 

![image](date-connects-result.png)

- Click on **aggregation** type minimum and drag on the canvas (It allows to combine of two similarities computed by the comparators)

![image](aggregation.png)

- Drag the little dot on the right side of string equality and date operators onto the left dot of the aggregation box(minimum) to connect the two with a line (you always must drag from the right side of one element to the left side of another to connect the two).

![image](equality-aggregation.png)

- Click on **save** on the right side of the page.

![image](click-on-save.png)

### **Export Result: Linking evaluation.**

- Click on the **linking evaluation**.

![image](click-on-evalution.png)

-  Click on the **play button** to start the evaluation and generate the links.

![image](click-on-play.png)

**Step Result**: The links are generated as shown below. (It allows us to review the links and since Data Integration does not know which column to use as a unique identifier, it just uses the row number in the .csv file to identify each movie.

![image](result.png)

- Click on the **linking execution** then click on the play button to execute the links (It copies the links to our data file links.csv (which is our output file).

![image](click-on-linkexe.png)

**Step Result**: The links are executed and copied to the output data file links.csv, showing the count of links on the page.

![image](click-on-linkexe.png)