#pragma once
#include <Comment.h>
#include <Notif.h>
#include <string>
#include <vector>

class API
{
private:
    std::string auth_token;
    std::string auth_key;
    int user_id;

public:
    API();
    ~API();

    bool login(std::string username, std::string password);
    std::vector<Notif> getNotifs();
    Comment getComment(int comment_id);
    bool postComment(std::string comment, int rant_id);
    bool clearNotifs();
};
