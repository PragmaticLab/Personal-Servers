//http://www.careercup.com/question?id=5168164910399488
#include <iostream>
#include <unordered_map>
#include <string>
#include <stdlib.h> // for the atoi
#include <vector>
#include <stdio.h>

using namespace std;

class URLShortener
{
   	private:
   	int key;
   	unordered_map <int, string> m;	
   	
   	public:
   	URLShortener ()
   	{
   		key = -1;
   	}

   	string put(string url)
   	{
   		key ++;
   		m[key] = url;
   		return std::to_string(key);
   	}

   	string get(string key)
   	{
   		try{
   			int this_key = atoi (key.c_str());
   			return m[this_key];
   		}catch (...)
   		{
   			return "404";
   		}
   	}

   	bool del(string key)
   	{
   		try{
   			int this_key = atoi (key.c_str());
   			m.erase(this_key);
   			return true;
   		}catch(...)
   		{
   			return false;
   		}
   	}

};


int main(int argc, char* argv[])
{
	URLShortener t;
	std::string google = "google.com";
	int key1 = t.put(google);
	std::string yahoo = "yahoo.com";
	int key2 = t.put(yahoo);

	cout << "ASD" << endl;

    return 0;
}

