# .gitdiff

This python script automates copying contents of git diff of staged files to your clipboard, its mainly used for generating AI prompts.

## Prerequisites

- Bash shell
- Python 3

## Instructions: 

1.  **Navigate to the Root Directory**

    Change directory to root. Run the following command in your terminal:

    ```bash
    cd
    ```

2.  **Clone the Repository**

    First, clone the repository to your local machine. Open a new terminal and run the following command:

    ```bash
    git clone git@github.com:gediminasnn/.gitdiff.git
    ```

    Optionally replace `git@github.com:gediminasnn/.gitdiff.git` with the actual URL of the repository.

3. **Determine Your Root Path**

    Run the following command in your terminal to determine your root path:

    ```bash
    pwd
    ```

    Note the output of this command as it will be used in the next step.

4. **Open Your Shell Configuration File**    
    
    Open your `.bashrc` or `.zshrc` file using a text editor by running the following command in your terminal:

    ```bash
    vim ~/.bashrc
    ```
    or
    ```bash
    vim ~/.zshrc
    ```

    Optionally replace `vim` with your favorite text editor.

5. **Add Execution Function To The Configuration File**
    
    Add the following command function to the end of your `.bashrc` or `.zshrc` file:

    ```bash
    gitdiff() {
        python3 /home/gediminas/.gitdiff/app.py
    }
    ```

    **Replace `/home/gediminas/.copyfiles/app.py` with the output from the `pwd` command.**

6. **Save The Configuration File**

    After adding the function, you need to save the changes you made to your `.bashrc` or `.zshrc` file. In `vim`, you can do this by pressing `Esc`, typing `:wq`, and then pressing `Enter`. This will write the changes to the file and quit the editor. If you are using a different text editor, follow the appropriate steps to save the file.


7. **Refresh Your Terminal Configuration**

    After modifying your `.bashrc` or `.zshrc` file, the changes might not be reflected immediately in your current terminal session. To ensure the script and alias are available, run the following command in your terminal:

    ```bash
    source ~/.bashrc
    ```
    or
    ```bash
    source ~/.zshrc
    ```

    By completing this step, the `copyfiles` function will be available in your terminal whenever you need to copy the file contents and additional text to the clipboard.

## Usage

1. **Navigate to your desired project's directory source**

    For example run in your terminal: 

    ```bash
    cd /home/gediminas/exchange-portal
    ```

2. **Add your desired custom text to `append_text.txt`**

    Example of `append_text.txt`
    ```
    ___________________________________________________________________
    Above I provided the whole gitdiff that I have staged, please provide clean git commit name for it 
    ___________________________________________________________________ 
    ```

3. **Copy file contents**

    Simply run in the terminal:

    ```bash
    gitdiff
    ```

    **Example output:**

    ```bash
    diff --git a/append_text.txt b/append_text.txt
    index e69de29..3d2c246 100644
    --- a/append_text.txt
    +++ b/append_text.txt
    @@ -0,0 +1,3 @@
    +___________________________________________________________________
    +Above I provided the whole codebase that I have currently
    +___________________________________________________________________ 
    ___________________________________________________________________
    Above I provided the whole gitdiff that I have staged, please provide clean git commit name for it 
    ___________________________________________________________________ 
    ```

## License

This project is licensed under the MIT License
