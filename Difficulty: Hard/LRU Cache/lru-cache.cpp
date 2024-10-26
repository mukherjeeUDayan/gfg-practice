//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// design the class in the most optimal way

class LRUCache {
  private:
    struct Node {
        int key;
        int value;
        Node* prev;
        Node* next;

        Node(int k, int v) {
            key = k;
            value = v;
            prev = NULL;
            next = NULL;
        }
    };
    unordered_map<int, Node*> mp;
    int capacity;
    Node* head;
    Node* tail;
    
    void add(Node* node) {
        Node* nextNode = head->next;
        head->next = node;
        node->next = nextNode;
        node->prev = head;
        nextNode->prev = node;
    }

    void remove(Node* node) {
        Node* prevNode = node->prev;
        Node* nextNode = node->next;
        prevNode->next = nextNode;
        nextNode->prev = prevNode;
    }
  public:
    // Constructor for initializing the cache capacity with the given value.
    LRUCache(int cap) {
        this->capacity = cap;
        head = new Node(-1, -1);
        tail = new Node(-1, -1);
        head->next = tail;
        tail->prev = head;// code here
    }

    // Function to return value corresponding to the key.
    int get(int key) {
        // your code here
        if (mp.find(key) == mp.end())
            return -1;
        Node* node = mp[key];
        remove(node);
        add(node);
        return node->value;
    }

    // Function for storing key-value pair.
    void set(int key, int value) {
        // your code here
        if (mp.find(key) != mp.end()) {
            Node* getNode = mp[key];
            remove(getNode);
        }
        Node* node = new Node(key, value);
        add(node);
        mp[key] = node;

        if (mp.size() > capacity) {
            Node* nodeToDelete = tail->prev;
            mp.erase(nodeToDelete->key);
            remove(nodeToDelete);
        }
    }
};

//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {

        int capacity;
        cin >> capacity;
        LRUCache *cache = new LRUCache(capacity);

        int queries;
        cin >> queries;
        while (queries--) {
            string q;
            cin >> q;
            if (q == "SET") {
                int key;
                cin >> key;
                int value;
                cin >> value;
                cache->set(key, value);
            } else {
                int key;
                cin >> key;
                cout << cache->get(key) << " ";
            }
        }
        cout << endl;

        cout << "~"
             << "\n";
    }
    return 0;
}

// } Driver Code Ends