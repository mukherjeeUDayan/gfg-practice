/*
class Node {
    int data;
    Node *left;
    Node *right;

    Node(int val) {
        data = val;
        left = right = NULL;
    }
};
*/
class Solution {
  public:
    vector<int> zigZagTraversal(Node* root) {
        // code here
        vector<int>ans;
        queue<Node*>q;
        q.push(root);
        bool flag = true;
        while(q.size()){
            vector<int>temp;
            int size = q.size();
            while(size--){
                auto elem = q.front();
                q.pop();
                temp.push_back(elem->data);
                if(elem->left)q.push(elem->left);
                if(elem->right)q.push(elem->right);
            }
            if(!flag)reverse(temp.begin(), temp.end());
            ans.insert(ans.end(), temp.begin(), temp.end());
            flag = !flag;
        }
        return ans;
    }
};