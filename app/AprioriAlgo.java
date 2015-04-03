import java.io.BufferedReader;
import java.io.FileReader;
import java.io.*;
import java.util.*;
public class AprioriAlgo
{
	int [][]dset;
	int[] arr= new int[30];
	Vector<String> candidates=new Vector<String>(); //the current candidates
	static Vector<String> candidatesCopy = new Vector<String>(); //the copy of
	String temp;
    int numItems; //number of items per transaction
    int numTransactions; //number of transactions
    float minSup; //minimum support for a frequent itemset
    String []attribs;
	public void AprioriAlgo(int n)
	{
		dset=new int[n][attribs.length];
	}
	void makedata(String fn)
	{
		BufferedReader fileReader = null;
		String line = "";
        //Create the file reader
        try
        {
        	fileReader = new BufferedReader(new FileReader(fn));
        	int rec=0;
        	attribs=(fileReader.readLine()).split(" ");
	        while ((line = fileReader.readLine()) != null)
	        {
	      		rec++;
	        }
	        this.AprioriAlgo(rec);
	        fileReader.close();
	        fileReader = new BufferedReader(new FileReader(fn));
	        int i=0;
	        fileReader.readLine();
	        while ((line = fileReader.readLine()) != null)
	        {
	            //Get all tokens available in line
	        	String[] tokens = line.split(" ");
	        	for(int j=0;j<tokens.length;j++)
	        		dset[i][j]=Integer.parseInt(tokens[j]);
	        	i++;
	        }
	    }
        catch (Exception e) {
            e.printStackTrace();
        }
        finally
        {
            try {
                fileReader.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
	}
	void showdata()
	{
		for(int i=0;i<dset.length;i++)
        {
        	for(int j=0;j<dset[i].length;j++)
        		System.out.print(" "+dset[i][j]);
        	System.out.println();
        }
	}

	public void AprioriAlgoProcess(String fp)
    {
        Date d; //date object for timing purposes
        long start, end; //start and end time
        int itemsetNumber=0; //the current itemset being looked at
        //System.out.println("Apriori algorithm has started.\n");

        //start timer
        d = new Date();
        start = d.getTime();
	makedata(fp);
      //  showdata();
        //while not complete
        do
        {
            //increase the itemset that is being looked at
            itemsetNumber++;

            //generate the candidates
            generateCandidates(itemsetNumber);

            //determine and display frequent itemsets
            calculateFrequentItemsets(itemsetNumber);
            if(candidates.size()!=0)
            {
                //System.out.println("Frequent " + itemsetNumber + "-itemsets");
                //System.out.println(candidates);
            	temp = candidates.toString();
            	temp = temp.replace(",","");
            	//temp = removeDuplicates(temp);
            	//System.out.println(temp);
            }


        //if there are <=1 frequent items, then its the end. This prevents reading through the database again. When there is only one frequent itemset.
        }while(candidates.size()>1);
		candidatesCopy.add(temp);
        //end timer
        d = new Date();
        end = d.getTime();

        //display the execution time
        System.out.println("\nFor support "+minSup+" Execution time is: "+((double)(end-start)/1000) + " seconds.");

    }
	public static String removeDuplicates(String str) {
		boolean seen[] = new boolean[256];
		StringBuilder sb = new StringBuilder(seen.length);

		for (int i = 0; i < str.length(); i++) {
		    char ch = str.charAt(i);
		    if (!seen[ch]) {
		        seen[ch] = true;
		        sb.append(ch);
		    }
		}

		return sb.toString();
	}
	private void generateCandidates(int n)
    {
        Vector<String> tempCandidates = new Vector<String>(); //temporary candidate string vector
        String str1, str2; //strings that will be used for comparisons
        StringTokenizer st1, st2; //string tokenizers for the two itemsets being compared

        //if its the first set, candidates are just the attribs
        if(n==1)
        {
            for(int i=0; i<attribs.length; i++)
            {
                tempCandidates.add(attribs[i]);//Integer.toString(i));
            }
        }
        else if(n==2) //second itemset is just all combinations of itemset 1
        {
            //add each itemset from the previous frequent itemsets together
            for(int i=0; i<candidates.size(); i++)
            {
                st1 = new StringTokenizer(candidates.get(i));
                str1 = st1.nextToken();
                for(int j=i+1; j<candidates.size(); j++)
                {
                    st2 = new StringTokenizer(candidates.elementAt(j));
                    str2 = st2.nextToken();
                    tempCandidates.add(str1 + " " + str2);
                }
            }
        }
        else
        {
            //for each itemset
            for(int i=0; i<candidates.size(); i++)
            {
                //compare to the next itemset
                for(int j=i+1; j<candidates.size(); j++)
                {
                    //create the strigns
                    str1 = new String();
                    str2 = new String();
                    //create the tokenizers
                    st1 = new StringTokenizer(candidates.get(i));
                    st2 = new StringTokenizer(candidates.get(j));

                    //make a string of the first n-2 tokens of the strings
                    for(int s=0; s<n-2; s++)
                    {
                        str1 = str1 + " " + st1.nextToken();
                        str2 = str2 + " " + st2.nextToken();
                    }

                    //if they have the same n-2 tokens, add them together
                    if(str2.compareToIgnoreCase(str1)==0)
                        tempCandidates.add((str1 + " " + st1.nextToken() + " " + st2.nextToken()).trim());
                }
            }
        }
        //clear the old candidates
        candidates.clear();
        //set the new ones
        candidates = new Vector<String>(tempCandidates);
        tempCandidates.clear();
    }

	private void calculateFrequentItemsets(int n)
    {
        Vector<String> frequentCandidates = new Vector<String>(); //the frequent candidates for the current itemset
        StringTokenizer st; //tokenizer for candidate and transaction
        boolean match; //whether the transaction has all the items in an itemset
        //boolean trans[] = new boolean[attribs.length]; //array to hold a transaction so that can be checked
        int count[] = new int[candidates.size()]; //the number of successful matches

                //for each transaction
                for(int i=0; i<dset.length;i++)//numTransactions; i++)
                {
                    int ind;
                    //check each candidate
                    for(int c=0; c<candidates.size(); c++)
                    {
                        match = false; //reset match to false
                        //tokenize the candidate so that we know what items need to be present for a match
                        st = new StringTokenizer(candidates.get(c));
                        //check each item in the itemset to see if it is present in the transaction
                        while(st.hasMoreTokens())
                        {
                            String s=st.nextToken();
                            for(ind=0;!(attribs[ind].equals(s));ind++);
                            if(dset[i][ind]==1)
                            	match=true;
                            else
                            	match=false;
                        	if(!match) //if it is not present in the transaction stop checking
                                break;
                        }
                        if(match) //if at this point it is a match, increase the count
                            count[c]++;
                    }

                }

                numTransactions=dset.length;
                for(int i=0; i<candidates.size(); i++)
                {
                    //  System.out.println("Candidate: " + candidates.get(c) + " with count: " + count + " % is: " + (count/(double)numItems));
                    //if the count% is larger than the minSup%, add to the candidate to the frequent candidates
                    if((count[i]/(double)numTransactions)>=minSup)
                    {
                        frequentCandidates.add(candidates.get(i));
                    }
                }
        //clear old candidates
        candidates.clear();
        //new candidates are the old frequent candidates
        candidates = new Vector<String>(frequentCandidates);
        frequentCandidates.clear();

     }
    private void display(){
    int i=0, j=0;
     for(i=0;i<27;i++){
		arr[j] = 0;
        }

        for (i=0;i<37;i++){
        	for(j=0;j<27;j++){
        		if(dset[i][j] == 1){
        			arr[j]= arr[j]+1;
        			///System.out.println(dset[i][j]);

        		}
        		//System.out.print(dset[i][j]+"\t");
              	}
              		//System.out.print("\n");
        }

     	System.out.println("");

    }
	public static void main(String[] args) throws IOException
    {
        //Input file which needs to be parsed
        String fileToParse;//="aprtest";//"datasetbin";
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        System.out.print("\nEnter Transaction Database File Name (Data in Binary form) : ");
        fileToParse="../assets/dataset1.0.csv";
        AprioriAlgo ap=new AprioriAlgo();
        double i;
        String a;
        int j=0;
        String temp;
        for ( i=0.9; i>0.4; i = i-0.1){
	        ap.minSup=(float)i;
	        ap.AprioriAlgoProcess(fileToParse);
       }

        for (int k=0; k<ap.candidatesCopy.size(); k= k+1){
    		System.out.println( k +"===>" + ap.candidatesCopy.get(k));
        	if(ap.candidatesCopy.get(k).indexOf("C20") == -1){
        		System.out.println("\nRemoving " + ap.candidatesCopy.get(k));
        		ap.candidatesCopy.remove(k);
        		k--;
        	}
     	}
     	for (int z = 0; z< ap.candidatesCopy.size(); z++){
     		for(int q =1; q<ap.candidatesCopy.size(); q++){
     			if(ap.candidatesCopy.get(z).length() > ap.candidatesCopy.get(q).length()){
     				      Collections.swap(ap.candidatesCopy, z, q);
     			}
     		}
     	}
			ap. display();
			System.out.println("\n This is optimal class atrribute \n") ;
     		System.out.print("\n"+ap.candidatesCopy.get(0)+"\n");
			for(int x=0;x<27;x++){
	        	System.out.print(ap.arr[x]+"\t");
        	}
	        	System.out.print("\n");
     }
}
