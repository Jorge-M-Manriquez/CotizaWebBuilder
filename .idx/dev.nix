# To learn more about how to use Nix to configure your environment
# see: https://developers.google.com/idx/guides/customize-idx-env
{ pkgs, ... }: {
  # Which nixpkgs channel to use.
  channel = "stable-23.11"; # or "unstable"

  # Use https://search.nixos.org/packages to find packages
  packages = [
    pkgs.python311
    pkgs.python311Packages.pip   # Agregar pip para instalar dependencias
    pkgs.nodejs_20
  ];

  # Sets environment variables in the workspace
  env = {
    VENV_DIR = ".venv";         # Directorio para el entorno virtual de Python
    MAIN_FILE = "main.py";       # Archivo principal a ejecutar
  };

  idx = {
    # Enable previews
    previews = {
      enable = true;
      previews = {
        web = {
          # Ejecutar el servidor web
          command = [
            "bash"
            "-c"
            ''
            if [ ! -d $VENV_DIR ]; then
              echo "Virtual environment not found. Creating one..."
              python -m venv $VENV_DIR   # Crear el entorno virtual
            fi

            source $VENV_DIR/bin/activate  # Activar el entorno virtual

            if [ ! -f requirements.txt ]; then
              echo "requirements.txt not found. Creating one with flet..."
              echo "flet" > requirements.txt
            fi

            pip install -r requirements.txt  # Instalar las dependencias
            flet run $MAIN_FILE --web --port $PORT
            ''
          ];
          env = { PORT = "$PORT"; };
          manager = "web";
        };
      };
    };

    # Workspace lifecycle hooks
    workspace = {
      # Runs when a workspace is first created
      onCreate = {
        # Crear el entorno virtual e instalar dependencias
        create-venv = ''
          python -m venv $VENV_DIR   # Crear el entorno virtual

          if [ ! -f requirements.txt ]; then
            echo "requirements.txt not found. Creating one with flet..."
            echo "flet" > requirements.txt
          fi

          # Activar el entorno virtual e instalar dependencias
          source $VENV_DIR/bin/activate
          pip install -r requirements.txt
        '';

        # Abrir los archivos principales automáticamente
        default.openFiles = [ "README.md" "requirements.txt" "$MAIN_FILE" ];
      };

      # Runs when the workspace is (re)started
      onStart = {
        # Comprobar la existencia del entorno virtual y crear uno si es necesario
        check-venv-existence = ''
          if [ ! -d $VENV_DIR ]; then
            echo "Virtual environment not found. Creating one..."
            python -m venv $VENV_DIR
          fi

          if [ ! -f requirements.txt ]; then
            echo "requirements.txt not found. Creating one with flet..."
            echo "flet" > requirements.txt
          fi

          # Activar el entorno virtual e instalar dependencias
          source $VENV_DIR/bin/activate
          pip install -r requirements.txt
        '';

        # Abrir los archivos principales automáticamente
        default.openFiles = [ "README.md" "requirements.txt" "$MAIN_FILE" ];
      };
    };
  };
}
