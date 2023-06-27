{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "468c6c9a-acc8-4165-a207-76ef21c83153",
   "metadata": {},
   "outputs": [],
   "source": [
    "#import panda to be able to read in our budget data files \n",
    "import csv\n",
    "from pathlib import Path"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "0dcd1535-9ce4-494c-b2b7-03fdb9199ffc",
   "metadata": {},
   "outputs": [],
   "source": [
    "#variables that we will be monitoring \n",
    "total_months = 0\n",
    "prev_revenue = 0\n",
    "month_change = []\n",
    "net_change_list = []\n",
    "total = []\n",
    "net_profit = 0\n",
    "greatest_increase = [\"\", 0]\n",
    "greatest_decrease = [\"\", 9999999999999]\n",
    "total_revenue = 0 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "37432738-fc93-41c3-8662-7475c3c9d505",
   "metadata": {},
   "outputs": [],
   "source": [
    "#file paths for the two files we'll be working with: one will read in the file to load budget data, and the other is a text file where we'll send budget analysis.\n",
    "csvpath = Path(\"./Resources/budget_data.csv\")\n",
    "file_to_output = (\"./analysis.txt\")\n",
    "\n",
    "#opening the file to import path specified previously\n",
    "with open(csvpath, \"r\") as budget_file:\n",
    "    reader = csv.reader(budget_file,delimiter=\",\")\n",
    "    first_row = next(reader)\n",
    "    #iterate through each row in the dataset. \n",
    "    for row in reader:\n",
    "        #Calculating the number of rows will yield the total number of months.\n",
    "        total_months = total_months + 1\n",
    "        total_revenue = total_revenue + int(row[1])         \n",
    "        net_change = int(row[1]) - prev_revenue\n",
    "        prev_revenue = int(row[1])\n",
    "        net_change_list = net_change_list + [net_change]\n",
    "        month_change = month_change + [row[0]] \n",
    "        \n",
    "    #calculating the greatest increase, Comparing the change in revenue to the greatest increase at 1\n",
    "        if (net_change > greatest_increase[1]):\n",
    "            greatest_increase[0] = row[0]\n",
    "            greatest_increase[1] = net_change\n",
    "    \n",
    "    #calculating the greatest decrease, Comparing the change in revenue to the greatest increase at 1\n",
    "        if (net_change < greatest_decrease[1]):\n",
    "            greatest_decrease[0] = row[0]\n",
    "            greatest_decrease[1] = net_change\n",
    "            \n",
    "#total of each of the revenue change list values that we were appending,the average will be calculated by dividing the total by the number of items on the revenue change list.            \n",
    "monthly_profit = round(sum(net_change_list) / len(net_change_list), 2)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "7ccd63a4-f9b8-4e74-881b-5c83c3945c66",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "-----------------------\n",
      "Total Months: 86\n",
      "Total: 38382578\n",
      "Average Change: 7803.48\n",
      "Greatest Increase in Profit: Feb-2012 ($1926159)\n",
      "Greatest decrease in Profit: Sep-2013 ($-2196167)\n"
     ]
    }
   ],
   "source": [
    "print(f\"Financial Analysis\")\n",
    "print(f\"-----------------------\")\n",
    "print(f\"Total Months: {total_months}\")\n",
    "print(f\"Total: {total_revenue}\")\n",
    "print(f\"Average Change: {monthly_profit}\")\n",
    "print(f\"Greatest Increase in Profit: {greatest_increase[0]} (${greatest_increase[1]})\")\n",
    "print(f\"Greatest decrease in Profit: {greatest_decrease[0]} (${greatest_decrease[1]})\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "655f97a1-2f77-4a78-aab1-cf22527e4dfa",
   "metadata": {},
   "outputs": [],
   "source": [
    "#file to output is the path we specified for the output file earlier.\n",
    "with open(file_to_output, \"w\") as txt_file:\n",
    "    txt_file.write(f\"Financial Analysis\\n\")\n",
    "    txt_file.write(f\"-----------------------\\n\")\n",
    "    txt_file.write(f\"Total Months: {total_months}\\n\")\n",
    "    txt_file.write(f\"Total: {total_revenue}\\n\")\n",
    "    txt_file.write(f\"Average Change: {monthly_profit}\\n\")\n",
    "    txt_file.write(f\"Greatest Increase in Profit: {greatest_increase[0]} (${greatest_increase[1]})\\n\")\n",
    "    txt_file.write(f\"Greatest decrease in Profit: {greatest_decrease[0]} (${greatest_decrease[1]})\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "2b33e21e-3a92-43d7-b9d1-640bafe1a71c",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "#citation:\n",
    "#   1.https://careerkarma.com/blog/python-valueerror-invalid-literal-for-int-with-base-10/\n",
    "#   2.https://stackoverflow.com/questions/32554527/typeerror-list-indices-must-be-integers-or-slices-not-str\n",
    "#   3.https://stackoverflow.com/questions/26685679/typeerror-unsupported-operand-types-for-list-and-list\n",
    "#   4.https://stackoverflow.com/questions/18952716/valueerror-i-o-operation-on-closed-file\n",
    "#   5.https://stackoverflow.com/questions/42364690/indentationerror-expected-an-indented-block-opening-csv-file\n",
    "#   6.https://www.youtube.com/watch?v=HnwrNrMv03g&list=PLBNHcTwrlK2h-3_kPuZo597i3mMUOA0oe&index=1"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
