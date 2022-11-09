#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <iterator>
#include <list>
using namespace std;

string slice(string orignal_str, int index)
{
    string accumulate = "";

    for (int i = 0; i < index; i++)
        accumulate += orignal_str[i];

    return accumulate;
}

void print_lst(list<tuple<string, int>> arr)
{
    list<tuple<string, int>>::iterator iter = arr.begin();

    for (; iter != arr.end(); iter++)
    {
        cout << "STR: " << get<0>(*iter) << ' ' << "UNIQ: " << get<1>(*iter);
        cout << endl;
    }
    cout << endl;
}

bool comp_one(tuple<string, int>& a, tuple<string, int>& b)
{
    string val_a = get<0>(a);
    string val_b = get<0>(b);
    if (val_b.size() > val_a.size())
    {
        if (slice(val_b, val_a.size()) == val_a)
            return true;
    }
    if (val_b.size() < val_a.size())
    {
        if (slice(val_a, val_b.size()) == val_b)
            return false;
    }
    return false;
}

bool comp_two(tuple<string, int>& a, tuple<string, int>& b)
{
    string val_a = get<0>(a);
    string val_b = get<0>(b);

    if (val_b.size() > val_a.size())
    {
        for (int min_s = 0; min_s < val_a.size(); min_s++)
        {
            if (val_a[min_s] != val_b[min_s])
                if (val_a[min_s] < val_b[min_s]) return true;
                else return false;
            
        }
    }
    if (val_b.size() < val_a.size())
    {
        for (int min_s = 0; min_s < val_a.size(); min_s++)
        {
            if (val_a[min_s] != val_b[min_s])
                if (val_a[min_s] < val_b[min_s]) return true;
                else return false;

        }
    }
    return false;
}

int quntity_unique(string str)
{
    set<char> prom_set;

    for (int i = 0; i < str.size(); i++)
        prom_set.insert(str[i]);

    set<char>::iterator iter;
    map<char, int> dict_symbols;

    for (iter = prom_set.begin(); iter != prom_set.end(); iter++)
        dict_symbols[*iter] = 0;

    for (int j = 0; j < str.size(); j++)
    {
        map<char, int>::iterator temporary_iter = dict_symbols.find(str[j]);
        temporary_iter->second++;
    }

    map<char, int>::iterator temporary_iter = dict_symbols.begin();
    int unique = 0;

    for (temporary_iter; temporary_iter != dict_symbols.end(); temporary_iter++)
        if (temporary_iter->second == 1) unique++;

    return unique;
}

string give_str()
{
    ifstream fin("C:/Users/Дмитрий/Desktop/LR_3_InfoSecure.txt");

    string strh;
    string str;

    while (!fin.eof()) {
        getline(fin, strh);
        str += strh;
        if (!fin.eof()) {
            str += '\n';
        }
    }

    return str;
}

list<tuple<string, int>> arr_sub_str(string str)
{
    list<tuple<string, int>> general_list;
    int max_substr_size = str.size() - 1;

    for (int size = 1; size <= max_substr_size; size++)
    {
        for (int prime_str = 0; prime_str <= str.size(); prime_str++)
        {
            string prom_str;

            for (int start = prime_str, quantity = 0; start <= max_substr_size && quantity < size; quantity++, start++)
            {
                prom_str += str[start];
            }

            if (prom_str.size() == size)
                general_list.push_back(make_tuple(prom_str, quntity_unique(prom_str)));
        }
    }

    return general_list;

}

list<tuple<string, int>> arr_max_sub(list<tuple<string, int>> &arr) 
{
    tuple<string, int> max = (*arr.begin());

    list<tuple<string, int>>::iterator primary_iter = arr.begin();

    for (; primary_iter != arr.end(); primary_iter++)
        if (get<1>(*primary_iter) > get<1>(max))
            max =(*primary_iter);

    list<tuple<string, int>> max_arr; 

    primary_iter = arr.begin();

    for (; primary_iter != arr.end(); primary_iter++) 
        if (get<1>(*primary_iter) == get<1>(max))
            max_arr.push_back((*primary_iter)); 

    return max_arr;
}

tuple<string, int> least(list<tuple<string, int>> arr)
{
    arr.sort(comp_one);
    arr.sort(comp_two);
    cout << "SORT:" << endl;
    cout << '\n';
    print_lst(arr);
    return *arr.begin();
}


void main()
{
    string text = give_str(); 

    list<tuple<string, int>> lst = arr_sub_str(text); 

    list<tuple<string, int>> lst_max = arr_max_sub(lst); 

    cout << "ORIGINAL:" << endl;
    cout << '\n';
    print_lst(lst_max);

    tuple<string, int> result = least(lst_max);
    cout << "The minimum substring among the maximum:" << get<0>(result) << " " << "UNIQ:" << get<1>(result) << endl;
}

